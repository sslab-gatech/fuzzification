#include "llvm/Pass.h"
#include "llvm/IR/Function.h"
#include "llvm/IR/Module.h"
#include "llvm/IR/IRBuilder.h"
#include "llvm/IR/Constant.h"
#include "llvm/Support/raw_ostream.h"
#include "llvm/IR/LegacyPassManager.h"
#include "llvm/Transforms/IPO/PassManagerBuilder.h"
#include "llvm/IR/InstIterator.h"

#include "llvm/IR/Constants.h"
#include "llvm/IR/Instructions.h"
#include "llvm/ADT/Statistic.h"
#include "modify.h" //<---this modify func must always return int for switch

#include <unordered_map>
#include <unistd.h>
#include <iostream>
#include <fstream>
#include <string>

using namespace llvm;
using namespace std;

#define INSTFILE "INST_BB"

namespace {
  struct SkeletonPass: public FunctionPass {
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
          sleeptime_flt = stof(sleeptime);
          sleep_map.insert({xorid_int, sleeptime_flt});	  
        }
        myfile.close();
      }            
    }

    bool exist_key(int keyvalue){
      auto search = sleep_map.find(keyvalue);
        if(search != sleep_map.end()) {
          return true;
        } 
        else
          return false;
    }

    bool runOnFunction(Function &F) {

      // Define used function
      LLVMContext &Ctx = F.getContext();

      // type
      std::vector<Type*> IntParamType = {Type::getInt32Ty(Ctx)};
      Type *IntRetType = Type::getInt32Ty(Ctx);
      std::vector<Type*> DoubleParamType = {Type::getDoubleTy(Ctx)};
      Type *DoubleRetType = Type::getDoubleTy(Ctx);
      std::vector<Type*> FloatParamType = {Type::getFloatTy(Ctx)};
      Type *FloatRetType = Type::getFloatTy(Ctx);
      std::vector<Type*> BoolParamType = {Type::getInt8Ty(Ctx)};
      Type *BoolRetType = Type::getInt8Ty(Ctx);

      // Functions for modifying operand in branch
      FunctionType *ModIntType = FunctionType::get(IntRetType, IntParamType, false);
      Constant *ModIntFunc = F.getParent()->getOrInsertFunction("modifyInt", ModIntType);
      FunctionType *ModDoubleType = FunctionType::get(DoubleRetType, DoubleParamType, false);
      Constant *ModDoubleFunc = F.getParent()->getOrInsertFunction("modifyDouble", ModDoubleType);
      FunctionType *ModFloatType = FunctionType::get(FloatRetType, FloatParamType, false);
      Constant *ModFloatFunc = F.getParent()->getOrInsertFunction("modifyFloat", ModFloatType);
      FunctionType *ModBoolType = FunctionType::get(BoolRetType, BoolParamType, false);
      Constant *ModBoolFunc = F.getParent()->getOrInsertFunction("modifyBool", ModBoolType);

      // Functions for wrapping return operand
      FunctionType *WrapIntType = FunctionType::get(IntRetType, IntParamType, false);
      Constant *WrapIntFunc = F.getParent()->getOrInsertFunction("retWrapInt", WrapIntType);
      FunctionType *WrapDoubleType = FunctionType::get(DoubleRetType, DoubleParamType, false);
      Constant *WrapDoubleFunc = F.getParent()->getOrInsertFunction("retWrapDouble", WrapDoubleType);
      FunctionType *WrapFloatType = FunctionType::get(FloatRetType, FloatParamType, false);
      Constant *WrapFloatFunc = F.getParent()->getOrInsertFunction("retWrapFloat", WrapFloatType);

      //for (auto &B : F) {
      for (Function::iterator B = F.begin(), e = F.end(); B != e; ++B){
        bool do_inst = false;
        Instruction* inst = B->getFirstNonPHI();
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
              //TotalInsts++;
              //errs() << ci2->getSExtValue() << ",";
              do_inst = true; 
            }
          }
        }

        //https://www.inf.ed.ac.uk/teaching/courses/ct/17-18/slides/llvm-2-writing_pass.pdf
        for (BasicBlock::iterator I = B->begin(), e = B->end(); I != e; ++I){
          if (BranchInst* BI = dyn_cast<BranchInst>(&*I)) {

            if(BI->isConditional() && isa<CmpInst>(BI->getCondition()) && do_inst) {
              CmpInst * CI = dyn_cast<CmpInst>(BI->getCondition());

              Constant *currentConstantFunc = NULL;

              auto *opA = CI->getOperand(0);
              auto *opB = CI->getOperand(1);
              auto argsA = llvm::ArrayRef<llvm::Value *>(&opA, 1);
              auto argsB = llvm::ArrayRef<llvm::Value *>(&opB, 1);

              bool modify = false;
            
              //assuming both operands are of the same type for conditional
              if (opA->getType()->isDoubleTy()) {
                currentConstantFunc = ModDoubleFunc;  
                modify = true;
              } else if (opA->getType()->isIntegerTy(32)) {
                currentConstantFunc = ModIntFunc;
                modify = true;
              } else if (opA->getType()->isFloatTy()) {
                currentConstantFunc = ModFloatFunc;
                modify = true;
              } //add more type distinctions here such as ptr

              if (modify){
                auto *ciA = CallInst::Create(currentConstantFunc, argsA, "funcA", CI);
                auto *ciB = llvm::CallInst::Create(currentConstantFunc, argsB, "funcB", CI);
                
                StringRef handler = cast<CallInst>(ciA)->getCalledFunction()->getName();
                //errs() << handler.str() << "\n";
                CI->setOperand(0, ciA);
                CI->setOperand(1, ciB);                          
              }
            }          
          } 
        }
      }
      return false;
    }
  };
}

char SkeletonPass::ID = 0;
static RegisterPass<SkeletonPass> X("symb", "anti-symbolic",
                             false /* Only looks at CFG */,
                             false /* Analysis Pass */);

