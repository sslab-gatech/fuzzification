HUGE1 = """
#include <unistd.h>
#define MAXX 255

int global_size;


void f0(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f0\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f1(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f1\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f2(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f2\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f3(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f3\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f4(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f4\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f5(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f5\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f6(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f6\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f7(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f7\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f8(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f8\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f9(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f9\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f10(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f10\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f11(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f11\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f12(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f12\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f13(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f13\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f14(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f14\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f15(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f15\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f16(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f16\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f17(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f17\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f18(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f18\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f19(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f19\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f20(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f20\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f21(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f21\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f22(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f22\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f23(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f23\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f24(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f24\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f25(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f25\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f26(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f26\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f27(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f27\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f28(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f28\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f29(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f29\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f30(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f30\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f31(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f31\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f32(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f32\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f33(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f33\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f34(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f34\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f35(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f35\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f36(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f36\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f37(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f37\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f38(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f38\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f39(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f39\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f40(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f40\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f41(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f41\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f42(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f42\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f43(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f43\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f44(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f44\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f45(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f45\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f46(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f46\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f47(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f47\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f48(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f48\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f49(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f49\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f50(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f50\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f51(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f51\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f52(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f52\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f53(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f53\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f54(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f54\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f55(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f55\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f56(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f56\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f57(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f57\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f58(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f58\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f59(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f59\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f60(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f60\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f61(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f61\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f62(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f62\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f63(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f63\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f64(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f64\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f65(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f65\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f66(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f66\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f67(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f67\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f68(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f68\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f69(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f69\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f70(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f70\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f71(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f71\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f72(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f72\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f73(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f73\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f74(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f74\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f75(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f75\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f76(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f76\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f77(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f77\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f78(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f78\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f79(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f79\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f80(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f80\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f81(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f81\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f82(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f82\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f83(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f83\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f84(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f84\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f85(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f85\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f86(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f86\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f87(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f87\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f88(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f88\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f89(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f89\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f90(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f90\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f91(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f91\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f92(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f92\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f93(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f93\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f94(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f94\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f95(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f95\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f96(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f96\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f97(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f97\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f98(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f98\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f99(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f99\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f100(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f100\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f101(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f101\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f102(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f102\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f103(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f103\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f104(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f104\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f105(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f105\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f106(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f106\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f107(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f107\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f108(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f108\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f109(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f109\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f110(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f110\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f111(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f111\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f112(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f112\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f113(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f113\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f114(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f114\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f115(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f115\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f116(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f116\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f117(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f117\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f118(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f118\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f119(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f119\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f120(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f120\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f121(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f121\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f122(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f122\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f123(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f123\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f124(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f124\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f125(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f125\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f126(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f126\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f127(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f127\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f128(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f128\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f129(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f129\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f130(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f130\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f131(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f131\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f132(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f132\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f133(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f133\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f134(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f134\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f135(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f135\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f136(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f136\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f137(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f137\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f138(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f138\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f139(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f139\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f140(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f140\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f141(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f141\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f142(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f142\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f143(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f143\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f144(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f144\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f145(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f145\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f146(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f146\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f147(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f147\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f148(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f148\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f149(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f149\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f150(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f150\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f151(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f151\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f152(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f152\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f153(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f153\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f154(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f154\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f155(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f155\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f156(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f156\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f157(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f157\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f158(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f158\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f159(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f159\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f160(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f160\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f161(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f161\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f162(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f162\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f163(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f163\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f164(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f164\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f165(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f165\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f166(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f166\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f167(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f167\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f168(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f168\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f169(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f169\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f170(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f170\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f171(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f171\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f172(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f172\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f173(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f173\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f174(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f174\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f175(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f175\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f176(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f176\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f177(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f177\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f178(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f178\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f179(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f179\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f180(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f180\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f181(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f181\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f182(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f182\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f183(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f183\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f184(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f184\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f185(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f185\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f186(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f186\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f187(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f187\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f188(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f188\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f189(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f189\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f190(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f190\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f191(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f191\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f192(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f192\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f193(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f193\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f194(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f194\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f195(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f195\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f196(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f196\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f197(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f197\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f198(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f198\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f199(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f199\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f200(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f200\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f201(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f201\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f202(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f202\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f203(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f203\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f204(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f204\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f205(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f205\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f206(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f206\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f207(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f207\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f208(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f208\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f209(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f209\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f210(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f210\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f211(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f211\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f212(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f212\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f213(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f213\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f214(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f214\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f215(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f215\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f216(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f216\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f217(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f217\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f218(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f218\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f219(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f219\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f220(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f220\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f221(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f221\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f222(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f222\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f223(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f223\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f224(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f224\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f225(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f225\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f226(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f226\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f227(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f227\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f228(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f228\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f229(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f229\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f230(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f230\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f231(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f231\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f232(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f232\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f233(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f233\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f234(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f234\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f235(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f235\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f236(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f236\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f237(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f237\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f238(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f238\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f239(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f239\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f240(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f240\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f241(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f241\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f242(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f242\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f243(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f243\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f244(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f244\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f245(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f245\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f246(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f246\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f247(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f247\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f248(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f248\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f249(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f249\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f250(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f250\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f251(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f251\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f252(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f252\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f253(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f253\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f254(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f254\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


void f255(unsigned char* input, int index, void* jtable []){
#ifdef DEBUG
    printf("here: f255\\n");
    printf("current input: %d\\n", input[index]);
  //printf("next input: %d\\n", input[index+1]);
    printf("current index: %d\\n", index);
    printf("current addr: %p\\n", jtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jtable[abs(input[++index] % MAXX)];
        foo(input, index, jtable); 
    }
}


/*
void shuffle(int **array, size_t n)
{
    //srand(time(NULL));

  if (n > 1) 
  {
    size_t i;
    for (i = 0; i < n - 1; i++) 
    {
      size_t j = i + rand() / (RAND_MAX / (n - i) + 1);
      void* t = array[j];
      array[j] = array[i];
      array[i] = t;
    }
  }
}


*/

void huge_branch(unsigned char* input, int size){

    // overwrite input
    int max = MAXX;
  global_size = size;
    unsigned char str[max];
    for (int i=0;i<max;i++){
        if (i<size){
            unsigned char a = input[i];
            str[i] = a;
        }
        else{
            str[i] = i;
        }
    }
    unsigned char *newinput = (unsigned char *)malloc(strlen(str)+1);
  strcpy(newinput,str);

  void *jtable[MAXX];    
    jtable[0] = &f0;
    jtable[1] = &f1;
    jtable[2] = &f2;
    jtable[3] = &f3;
    jtable[4] = &f4;
    jtable[5] = &f5;
    jtable[6] = &f6;
    jtable[7] = &f7;
    jtable[8] = &f8;
    jtable[9] = &f9;
    jtable[10] = &f10;
    jtable[11] = &f11;
    jtable[12] = &f12;
    jtable[13] = &f13;
    jtable[14] = &f14;
    jtable[15] = &f15;
    jtable[16] = &f16;
    jtable[17] = &f17;
    jtable[18] = &f18;
    jtable[19] = &f19;
    jtable[20] = &f20;
    jtable[21] = &f21;
    jtable[22] = &f22;
    jtable[23] = &f23;
    jtable[24] = &f24;
    jtable[25] = &f25;
    jtable[26] = &f26;
    jtable[27] = &f27;
    jtable[28] = &f28;
    jtable[29] = &f29;
    jtable[30] = &f30;
    jtable[31] = &f31;
    jtable[32] = &f32;
    jtable[33] = &f33;
    jtable[34] = &f34;
    jtable[35] = &f35;
    jtable[36] = &f36;
    jtable[37] = &f37;
    jtable[38] = &f38;
    jtable[39] = &f39;
    jtable[40] = &f40;
    jtable[41] = &f41;
    jtable[42] = &f42;
    jtable[43] = &f43;
    jtable[44] = &f44;
    jtable[45] = &f45;
    jtable[46] = &f46;
    jtable[47] = &f47;
    jtable[48] = &f48;
    jtable[49] = &f49;
    jtable[50] = &f50;
    jtable[51] = &f51;
    jtable[52] = &f52;
    jtable[53] = &f53;
    jtable[54] = &f54;
    jtable[55] = &f55;
    jtable[56] = &f56;
    jtable[57] = &f57;
    jtable[58] = &f58;
    jtable[59] = &f59;
    jtable[60] = &f60;
    jtable[61] = &f61;
    jtable[62] = &f62;
    jtable[63] = &f63;
    jtable[64] = &f64;
    jtable[65] = &f65;
    jtable[66] = &f66;
    jtable[67] = &f67;
    jtable[68] = &f68;
    jtable[69] = &f69;
    jtable[70] = &f70;
    jtable[71] = &f71;
    jtable[72] = &f72;
    jtable[73] = &f73;
    jtable[74] = &f74;
    jtable[75] = &f75;
    jtable[76] = &f76;
    jtable[77] = &f77;
    jtable[78] = &f78;
    jtable[79] = &f79;
    jtable[80] = &f80;
    jtable[81] = &f81;
    jtable[82] = &f82;
    jtable[83] = &f83;
    jtable[84] = &f84;
    jtable[85] = &f85;
    jtable[86] = &f86;
    jtable[87] = &f87;
    jtable[88] = &f88;
    jtable[89] = &f89;
    jtable[90] = &f90;
    jtable[91] = &f91;
    jtable[92] = &f92;
    jtable[93] = &f93;
    jtable[94] = &f94;
    jtable[95] = &f95;
    jtable[96] = &f96;
    jtable[97] = &f97;
    jtable[98] = &f98;
    jtable[99] = &f99;
    jtable[100] = &f100;
    jtable[101] = &f101;
    jtable[102] = &f102;
    jtable[103] = &f103;
    jtable[104] = &f104;
    jtable[105] = &f105;
    jtable[106] = &f106;
    jtable[107] = &f107;
    jtable[108] = &f108;
    jtable[109] = &f109;
    jtable[110] = &f110;
    jtable[111] = &f111;
    jtable[112] = &f112;
    jtable[113] = &f113;
    jtable[114] = &f114;
    jtable[115] = &f115;
    jtable[116] = &f116;
    jtable[117] = &f117;
    jtable[118] = &f118;
    jtable[119] = &f119;
    jtable[120] = &f120;
    jtable[121] = &f121;
    jtable[122] = &f122;
    jtable[123] = &f123;
    jtable[124] = &f124;
    jtable[125] = &f125;
    jtable[126] = &f126;
    jtable[127] = &f127;
    jtable[128] = &f128;
    jtable[129] = &f129;
    jtable[130] = &f130;
    jtable[131] = &f131;
    jtable[132] = &f132;
    jtable[133] = &f133;
    jtable[134] = &f134;
    jtable[135] = &f135;
    jtable[136] = &f136;
    jtable[137] = &f137;
    jtable[138] = &f138;
    jtable[139] = &f139;
    jtable[140] = &f140;
    jtable[141] = &f141;
    jtable[142] = &f142;
    jtable[143] = &f143;
    jtable[144] = &f144;
    jtable[145] = &f145;
    jtable[146] = &f146;
    jtable[147] = &f147;
    jtable[148] = &f148;
    jtable[149] = &f149;
    jtable[50] = &f50;
    jtable[151] = &f151;
    jtable[152] = &f152;
    jtable[153] = &f153;
    jtable[154] = &f154;
    jtable[155] = &f155;
    jtable[156] = &f156;
    jtable[157] = &f157;
    jtable[158] = &f158;
    jtable[159] = &f159;
    jtable[160] = &f160;
    jtable[161] = &f161;
    jtable[162] = &f162;
    jtable[163] = &f163;
    jtable[164] = &f164;
    jtable[165] = &f165;
    jtable[166] = &f166;
    jtable[167] = &f167;
    jtable[168] = &f168;
    jtable[169] = &f169;
    jtable[170] = &f170;
    jtable[171] = &f171;
    jtable[172] = &f172;
    jtable[173] = &f173;
    jtable[174] = &f174;
    jtable[175] = &f175;
    jtable[176] = &f176;
    jtable[177] = &f177;
    jtable[178] = &f178;
    jtable[179] = &f179;
    jtable[180] = &f180;
    jtable[181] = &f181;
    jtable[182] = &f182;
    jtable[183] = &f183;
    jtable[184] = &f184;
    jtable[185] = &f185;
    jtable[186] = &f186;
    jtable[187] = &f187;
    jtable[188] = &f188;
    jtable[189] = &f189;
    jtable[190] = &f190;
    jtable[191] = &f191;
    jtable[192] = &f192;
    jtable[193] = &f193;
    jtable[194] = &f194;
    jtable[195] = &f195;
    jtable[196] = &f196;
    jtable[197] = &f197;
    jtable[198] = &f198;
    jtable[199] = &f199;
    jtable[200] = &f200;
    jtable[201] = &f201;
    jtable[202] = &f202;
    jtable[203] = &f203;
    jtable[204] = &f204;
    jtable[205] = &f205;
    jtable[206] = &f206;
    jtable[207] = &f207;
    jtable[208] = &f208;
    jtable[209] = &f209;
    jtable[210] = &f210;
    jtable[211] = &f211;
    jtable[212] = &f212;
    jtable[213] = &f213;
    jtable[214] = &f214;
    jtable[215] = &f215;
    jtable[216] = &f216;
    jtable[217] = &f217;
    jtable[218] = &f218;
    jtable[219] = &f219;
    jtable[220] = &f220;
    jtable[221] = &f221;
    jtable[222] = &f222;
    jtable[223] = &f223;
    jtable[224] = &f224;
    jtable[225] = &f225;
    jtable[226] = &f226;
    jtable[227] = &f227;
    jtable[228] = &f228;
    jtable[229] = &f229;
    jtable[230] = &f230;
    jtable[231] = &f231;
    jtable[232] = &f232;
    jtable[233] = &f233;
    jtable[234] = &f234;
    jtable[235] = &f235;
    jtable[236] = &f236;
    jtable[237] = &f237;
    jtable[238] = &f238;
    jtable[239] = &f239;
    jtable[240] = &f240;
    jtable[241] = &f241;
    jtable[242] = &f242;
    jtable[243] = &f243;
    jtable[244] = &f244;
    jtable[245] = &f245;
    jtable[246] = &f246;
    jtable[247] = &f247;
    jtable[248] = &f248;
    jtable[249] = &f249;
    jtable[250] = &f250;
    jtable[251] = &f251;
    jtable[252] = &f252;
    jtable[253] = &f253;
    jtable[254] = &f254;
    jtable[255] = &f255;

    //shuffle(jtable, MAXX);

    int index=0;
    void (*foo)(unsigned char*, int, void* []) = jtable[index];
    foo(newinput, index, jtable);
}

int huge_raw_input(char* file_name){

  FILE *fp;
  fp = fopen(file_name, "r");
  
  fseek(fp, 0, SEEK_END);
  long fsize = ftell(fp);
  fseek(fp, 0, SEEK_SET); 

  unsigned char *input1 = malloc(MAXX/2 + 1);
  unsigned char *input2 = malloc(MAXX/2 + 1);

  fread(input1, MAXX/2, 1, fp);
  lseek(fp, -(MAXX/2), SEEK_END);  
  fread(input2, MAXX/2, 1, fp);
  strcat (input1, input2);
  huge_branch(input1, MAXX); 

  return 0;
}

"""

HUGE2 = """huge_raw_input(argv[{0}]);
"""

import os, sys

filename = sys.argv[1]
huge1 = int( sys.argv[2] )
huge2 = int( sys.argv[3] )
argv_num = sys.argv[4]

HUGE2 = HUGE2.replace("{0}", argv_num)

f = open(filename, "r")
contents = f.readlines()
f.close()

contents.insert(huge2, HUGE2)
contents.insert(huge1, HUGE1)

f = open(filename, "w")
contents = "".join(contents)
f.write(contents)
f.close()
