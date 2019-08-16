#include "llvm/ADT/Statistic.h"

#include "llvm/Pass.h"
#include "llvm/IR/Function.h"
#include "llvm/Support/raw_ostream.h"
#include "llvm/IR/LegacyPassManager.h"
#include "llvm/IR/InstrTypes.h"
#include "llvm/Transforms/IPO/PassManagerBuilder.h"
#include "llvm/IR/IRBuilder.h"
#include "llvm/Transforms/Utils/BasicBlockUtils.h"
#include "llvm/IR/Module.h"
#include "llvm/IR/CallSite.h"

#include "llvm/Support/Debug.h"
#include "llvm/Support/ErrorHandling.h"
#include "llvm/Support/ManagedStatic.h"
#include "llvm/Support/raw_ostream.h"

#include <unordered_map>
#include <unistd.h>
#include <iostream>
#include <fstream>
#include <string>

using namespace llvm;
using namespace std;

#define INSTFILE "INST_BB"
//#define INSTEXIT

#define DEBUG_TYPE "instcount"
STATISTIC(TotalInsts, "Number of instrumentation");

namespace {
  struct SkeletonPass : public FunctionPass {
    static char ID;
    std::unordered_map<int, float> sleep_map;

    SkeletonPass() : FunctionPass(ID) {
      parse_inst_bb();      
    }

    void parse_inst_bb(){
      string xorid;
      string sleeptime;
      int xorid_int;
      float sleeptime_flt;

      ifstream myfile (INSTFILE);
      if (myfile.is_open())
      {
        while ( getline (myfile, xorid, ','))
        {
          getline(myfile, sleeptime);
          xorid_int = stoi(xorid);
          //errs() << "parse" << xorid << "\n";
          sleeptime_flt = stof(sleeptime);
          sleep_map.insert({xorid_int, sleeptime_flt});	  
        }
        myfile.close();
      }            
    }

    bool exist_key(int keyvalue){
      //errs() << keyvalue << "\n";
      auto search = sleep_map.find(keyvalue);
        if(search != sleep_map.end()) {
	  //errs() << "found" << "\n";
          return true;
        } 
        else
          return false;
    }

    virtual bool runOnFunction(Function &F) {

      // Get the function to call from our runtime library.
      LLVMContext &Ctx = F.getContext();
      std::vector<Type*> paramTypes = {Type::getInt32Ty(Ctx)};
      Type *retType = Type::getVoidTy(Ctx);
      Type *retIntType = Type::getInt32Ty(Ctx);
      
      // logop
      FunctionType *logFuncType = FunctionType::get(retType, paramTypes, false);
      Constant *logFunc = F.getParent()->getOrInsertFunction("logop", logFuncType);

      // printbb
      std::vector<Type*> paramTypes2 = {Type::getInt32Ty(Ctx)};
      FunctionType *bbFuncType = FunctionType::get(retType, paramTypes2, false);
      Constant *bbFunc = F.getParent()->getOrInsertFunction("print", bbFuncType);

      // slp (int)
      std::vector<Type*> paramTypes3 = {Type::getInt32Ty(Ctx)};
      FunctionType *uslpType = FunctionType::get(retIntType, paramTypes3, false);
      Constant *uslpFunc = F.getParent()->getOrInsertFunction("slp", uslpType);

      // change_global (int)
      std::vector<Type*> paramTypes4 = {Type::getInt32Ty(Ctx)};
      FunctionType *globalType = FunctionType::get(retIntType, paramTypes4, false);
      Constant *globalFunc = F.getParent()->getOrInsertFunction("change_global", uslpType);      


#ifdef  INSTEXIT
      for (auto &B : F) {
        for (auto &I : B) {

          // find exit() call
          CallSite cs(&I);
          if (cs.getInstruction()) {
            Value* called = cs.getCalledValue()->stripPointerCasts();
            if (Function* f = dyn_cast<Function>(called)){ 
              if (!strncmp("exit", f->getName().data(), 4) || !strncmp("error", f->getName().data(), 5)){
                //errs() << f->getName() << "\n";
                //auto *op = dyn_cast<CallInst>(&cs);
                IRBuilder<> builder(cs.getInstruction());
                

                builder.SetInsertPoint(&B, builder.GetInsertPoint());
                Value* args[] = {ConstantInt::get(Type::getInt32Ty(Ctx), 2, false)};
                builder.CreateCall(uslpFunc, args);
                errs() << "Instrument exit()" << "\n";
              }
            }
          }
        } 
      }

#else
      for (auto &B : F) {
        Instruction* inst = B.getFirstNonPHI();
        BasicBlock::iterator it(inst);
        ++it; //skip first load
        ++it; //skip second load

        if (auto *op = dyn_cast<BinaryOperator>(it)) {
          IRBuilder<> builder(op);
          if (op->getOpcode() == Instruction::Xor)
          {
            Value* rhs = op->getOperand(1);
            if (rhs->getValueID() != 18){
              continue;
            }
            ConstantInt *ci2 = dyn_cast<ConstantInt>(rhs); // random-xor value
            if (exist_key(ci2->getSExtValue())){
              TotalInsts++;
              //errs() << ci2->getSExtValue() << ",";

              // call delay()
              builder.SetInsertPoint(&B, ++builder.GetInsertPoint());
              Value* args[] = {ConstantInt::get(Type::getInt32Ty(Ctx), 0, false)};
              //builder.CreateCall(uslpFunc, args);
              Value* ret_slp = builder.CreateCall(uslpFunc, args);

              // change global_variable using return value
              builder.SetInsertPoint(&B, ++builder.GetInsertPoint());
              Value* args2[] = {ret_slp};
              builder.CreateCall(globalFunc, args2);
            }
          }
        }
      }

#endif
      return false;
    }
  };  
}

char SkeletonPass::ID = 0;
static void registerSkeletonPass(const PassManagerBuilder &,
                         legacy::PassManagerBase &PM) {
  PM.add(new SkeletonPass());
}
static RegisterPass<SkeletonPass> X("SkeletonPass", "test", false, false);
