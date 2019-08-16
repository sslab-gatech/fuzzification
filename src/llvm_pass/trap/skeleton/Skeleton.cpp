#include "llvm/ADT/Statistic.h"
#include <llvm/CodeGen/MachineInstrBuilder.h>
#include <llvm/Target/TargetMachine.h>
#include <llvm/Target/TargetInstrInfo.h>

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

#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */

#include <unordered_map>
#include <unistd.h>
#include <iostream>
#include <fstream>
#include <string>

using namespace llvm;
using namespace std;

//TODO: apply instrumentation on specified basicblock using ID
namespace {
  struct SkeletonPass : public FunctionPass {
    static char ID;    

    SkeletonPass() : FunctionPass(ID) {
    }

    virtual bool runOnFunction(Function &F) {

      // Get the function to call from our runtime library.
      LLVMContext &Ctx = F.getContext();

      //std::vector<Type*> paramTypes = {Type::getInt32Ty(Ctx)};      
      Type *retType = Type::getVoidTy(Ctx);
      Type *intretType = Type::getInt64Ty(Ctx);
      
      //std::vector<Type*> paramTypes2 = {Type::getInt32Ty(Ctx)};
      //FunctionType *remType = FunctionType::get(intretType, paramTypes2, false);
      //Constant *remFunc = F.getParent()->getOrInsertFunction("rem", remType);

      std::vector<Type*> paramTypes3 = {Type::getInt64Ty(Ctx)};
      FunctionType *uslpType = FunctionType::get(intretType, paramTypes3, false);
      Constant *uslpFunc = F.getParent()->getOrInsertFunction("markfunc", uslpType);

      std::vector<Type*> paramTypes4 = {Type::getInt64Ty(Ctx), Type::getInt64Ty(Ctx), Type::getInt64Ty(Ctx), Type::getInt64Ty(Ctx)};
      FunctionType *dummyType = FunctionType::get(retType, paramTypes4, false);
      Constant *dummyFunc = F.getParent()->getOrInsertFunction("dummy", dummyType);

      std::vector<Type*> paramTypes5 = {Type::getInt64Ty(Ctx)};
      FunctionType *uslpType2 = FunctionType::get(intretType, paramTypes5, false);
      Constant *uslpFunc2 = F.getParent()->getOrInsertFunction("dummy2", uslpType2);

      for (auto &B : F) {

        BasicBlock::iterator i, e;
        for (i = B.begin(), e = B.end(); i != e; ++i) {
          Instruction* inst = &*i;          

          if (F.isIntrinsic() || F.isDeclaration())
            continue;

          if (*inst->getOpcodeName() == 'r' && F.arg_size() > 0){

            IRBuilder<> builder(inst);
            builder.SetInsertPoint(&B, builder.GetInsertPoint());

            IntegerType * i64Type = llvm::IntegerType::getInt64Ty(F.getContext());
            IntegerType * i32Type = llvm::IntegerType::getInt32Ty(F.getContext());
            ConstantInt * allOne = ConstantInt::get(i64Type, 0x1111111111111111, false);

            Value * ret = nullptr;
            Value * ret2 = nullptr;
            Value * toXor = nullptr;

            bool isFirst = true;
            
            int counter=0;
            Function::const_arg_iterator fIter = F.arg_begin(), fIterEnd = F.arg_end();
            for (; fIter != fIterEnd; fIter++) {
              counter++;
              Argument *arg = const_cast<Argument*> (&(*fIter));
              //errs() << "\t" << *arg << "\n";

              Type * argType = arg->getType();

              if (argType->isIntegerTy()) {
                //errs() << "int" << "\n";
                toXor = builder.CreateZExtOrTrunc(arg, i64Type);
              } else if (argType->isPointerTy()) {
                //errs() << "pointer" << "\n";
                toXor = builder.CreatePtrToInt(arg, i64Type);
                //ret2 = builder.CreatePtrToInt(arg, i64Type);
              } else if (argType->isFloatTy() || argType->isDoubleTy() || argType->isX86_FP80Ty()) {
                //errs() << "long" << "\n";
                toXor = builder.CreateFPToUI(arg, i64Type);
              } else {
                //errs() << "else" << "\n";
                //errs() << *arg << "\n";
                llvm_unreachable("unsupported type, please add necessary code to support it");
              }

              if (isFirst) {
                //errs() << "createxor1" <<"\n";
                ret = builder.CreateXor(allOne, toXor);
                isFirst = false;
              } else {
                //errs() << "createxor2" <<"\n";
                ret = builder.CreateXor(ret, toXor);
              }
            }
            ConstantInt * num = ConstantInt::get(i64Type, 0xff, false);
            ConstantInt * zero64 = ConstantInt::get(i64Type, 0, false);
            ret2= builder.CreateURem((Value *)num, (Value *)num); // not robust
                        
            Value* markargs[] = {ConstantInt::get(Type::getInt64Ty(Ctx), 0xdd, false)};
            Value* dummyargs[] = {ret, 
              ConstantInt::get(Type::getInt64Ty(Ctx), 0xaa, false),
              ConstantInt::get(Type::getInt64Ty(Ctx), 0xbb, false),
              ConstantInt::get(Type::getInt64Ty(Ctx), 0xbb, false)
            };            

            if (counter>=0){
              builder.CreateCall(dummyFunc, dummyargs);
              builder.CreateCall(uslpFunc, markargs);
              builder.CreateCall(uslpFunc, markargs);
              builder.CreateCall(uslpFunc, markargs);
              builder.CreateCall(uslpFunc, markargs);
              builder.CreateCall(uslpFunc2, markargs);

            }
          }
        }
      }
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
