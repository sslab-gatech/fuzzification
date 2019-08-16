#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAXX 101

int global_size;

void f0(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f0\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}

void f1(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f1\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}

void f2(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f2\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f3(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f3\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f4(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f4\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f5(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f5\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f6(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f6\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f7(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f7\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f8(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f8\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f9(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f9\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f10(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f10\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f11(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f11\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f12(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f12\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f13(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f13\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f14(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f14\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f15(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f15\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f16(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f16\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f17(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f17\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f18(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f18\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f19(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f19\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f20(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f20\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f21(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f21\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f22(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f22\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f23(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f23\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f24(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f24\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f25(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f25\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f26(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f26\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f27(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f27\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f28(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f28\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f29(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f29\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f30(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f30\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f31(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f31\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f32(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f32\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f33(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f33\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f34(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f34\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f35(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f35\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f36(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f36\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f37(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f37\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f38(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f38\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f39(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f39\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f40(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f40\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f41(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f41\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f42(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f42\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f43(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f43\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f44(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f44\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f45(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f45\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f46(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f46\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f47(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f47\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f48(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f48\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f49(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f49\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f50(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f50\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f51(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f51\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f52(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f52\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f53(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f53\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f54(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f54\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f55(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f55\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f56(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f56\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f57(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f57\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f58(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f58\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f59(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f59\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f60(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f60\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f61(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f61\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f62(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f62\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f63(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f63\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f64(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f64\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f65(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f65\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f66(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f66\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f67(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f67\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f68(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f68\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f69(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f69\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f70(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f70\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f71(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f71\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f72(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f72\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f73(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f73\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f74(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f74\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f75(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f75\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f76(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f76\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f77(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f77\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f78(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f78\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f79(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f79\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f80(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f80\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f81(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f81\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f82(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f82\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f83(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f83\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f84(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f84\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f85(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f85\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f86(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f86\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f87(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f87\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f88(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f88\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f89(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f89\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f90(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f90\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f91(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f91\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f92(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f92\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f93(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f93\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f94(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f94\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f95(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f95\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f96(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f96\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f97(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f97\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f98(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f98\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f99(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f99\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f100(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f100\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f101(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f101\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f102(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f102\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f103(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f103\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f104(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f104\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f105(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f105\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f106(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f106\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f107(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f107\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f108(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f108\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f109(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f109\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f110(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f110\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f111(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f111\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f112(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f112\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f113(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f113\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f114(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f114\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f115(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f115\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f116(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f116\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f117(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f117\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f118(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f118\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f119(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f119\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f120(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f120\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f121(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f121\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f122(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f122\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f123(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f123\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f124(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f124\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f125(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f125\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f126(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f126\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f127(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f127\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f128(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f128\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f129(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f129\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f130(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f130\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f131(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f131\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f132(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f132\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f133(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f133\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f134(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f134\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f135(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f135\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f136(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f136\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f137(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f137\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f138(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f138\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f139(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f139\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f140(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f140\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f141(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f141\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f142(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f142\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f143(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f143\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f144(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f144\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f145(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f145\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f146(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f146\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f147(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f147\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f148(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f148\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f149(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f149\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f150(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f150\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f151(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f151\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f152(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f152\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f153(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f153\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f154(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f154\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f155(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f155\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f156(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f156\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f157(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f157\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f158(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f158\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f159(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f159\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f160(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f160\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f161(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f161\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f162(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f162\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f163(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f163\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f164(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f164\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f165(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f165\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f166(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f166\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f167(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f167\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f168(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f168\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f169(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f169\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f170(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f170\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f171(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f171\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f172(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f172\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f173(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f173\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f174(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f174\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f175(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f175\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f176(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f176\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f177(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f177\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f178(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f178\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f179(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f179\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f180(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f180\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f181(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f181\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f182(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f182\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f183(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f183\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f184(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f184\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f185(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f185\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f186(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f186\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f187(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f187\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f188(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f188\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f189(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f189\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f190(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f190\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f191(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f191\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f192(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f192\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f193(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f193\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f194(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f194\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f195(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f195\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f196(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f196\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f197(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f197\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f198(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f198\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f199(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f199\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f200(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f200\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f201(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f201\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f202(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f202\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f203(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f203\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f204(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f204\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f205(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f205\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f206(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f206\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f207(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f207\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f208(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f208\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f209(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f209\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f210(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f210\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f211(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f211\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f212(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f212\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f213(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f213\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f214(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f214\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f215(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f215\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f216(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f216\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f217(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f217\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f218(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f218\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f219(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f219\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f220(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f220\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f221(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f221\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f222(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f222\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f223(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f223\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f224(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f224\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f225(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f225\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f226(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f226\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f227(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f227\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f228(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f228\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f229(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f229\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f230(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f230\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f231(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f231\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f232(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f232\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f233(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f233\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f234(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f234\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f235(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f235\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f236(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f236\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f237(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f237\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f238(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f238\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f239(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f239\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f240(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f240\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f241(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f241\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f242(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f242\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f243(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f243\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f244(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f244\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f245(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f245\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f246(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f246\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f247(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f247\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f248(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f248\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f249(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f249\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f250(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f250\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f251(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f251\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f252(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f252\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f253(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f253\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f254(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f254\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
    }
}


void f255(unsigned char* input, int index, void* jjtable []){
#ifdef DEBUG
    printf("here: f255\n");
    printf("current input: %d\n", input[index]);
  //printf("next input: %d\n", input[index+1]);
    printf("current index: %d\n", index);
    printf("current addr: %p\n", jjtable[abs(input[index] % MAXX)] );
#endif  
    if (index < global_size){       
        void (*foo)(unsigned char*, int, void* []) = jjtable[abs(input[++index] % MAXX)];
        foo(input, index, jjtable); 
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

void huge_branch(unsigned char* newinput, int size){

    // overwrite input
    int max = MAXX;
    global_size = size;

    /*
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
    */


  void *jjtable[MAXX];    
    jjtable[0] = &f0;
    jjtable[1] = &f1;
    jjtable[2] = &f2;
    jjtable[3] = &f3;
    jjtable[4] = &f4;
    jjtable[5] = &f5;
    jjtable[6] = &f6;
    jjtable[7] = &f7;
    jjtable[8] = &f8;
    jjtable[9] = &f9;
    jjtable[10] = &f10;
    jjtable[11] = &f11;
    jjtable[12] = &f12;
    jjtable[13] = &f13;
    jjtable[14] = &f14;
    jjtable[15] = &f15;
    jjtable[16] = &f16;
    jjtable[17] = &f17;
    jjtable[18] = &f18;
    jjtable[19] = &f19;
    jjtable[20] = &f20;
    jjtable[21] = &f21;
    jjtable[22] = &f22;
    jjtable[23] = &f23;
    jjtable[24] = &f24;
    jjtable[25] = &f25;
    jjtable[26] = &f26;
    jjtable[27] = &f27;
    jjtable[28] = &f28;
    jjtable[29] = &f29;
    jjtable[30] = &f30;
    jjtable[31] = &f31;
    jjtable[32] = &f32;
    jjtable[33] = &f33;
    jjtable[34] = &f34;
    jjtable[35] = &f35;
    jjtable[36] = &f36;
    jjtable[37] = &f37;
    jjtable[38] = &f38;
    jjtable[39] = &f39;
    jjtable[40] = &f40;
    jjtable[41] = &f41;
    jjtable[42] = &f42;
    jjtable[43] = &f43;
    jjtable[44] = &f44;
    jjtable[45] = &f45;
    jjtable[46] = &f46;
    jjtable[47] = &f47;
    jjtable[48] = &f48;
    jjtable[49] = &f49;
    jjtable[50] = &f50;
    jjtable[51] = &f51;
    jjtable[52] = &f52;
    jjtable[53] = &f53;
    jjtable[54] = &f54;
    jjtable[55] = &f55;
    jjtable[56] = &f56;
    jjtable[57] = &f57;
    jjtable[58] = &f58;
    jjtable[59] = &f59;
    jjtable[60] = &f60;
    jjtable[61] = &f61;
    jjtable[62] = &f62;
    jjtable[63] = &f63;
    jjtable[64] = &f64;
    jjtable[65] = &f65;
    jjtable[66] = &f66;
    jjtable[67] = &f67;
    jjtable[68] = &f68;
    jjtable[69] = &f69;
    jjtable[70] = &f70;
    jjtable[71] = &f71;
    jjtable[72] = &f72;
    jjtable[73] = &f73;
    jjtable[74] = &f74;
    jjtable[75] = &f75;
    jjtable[76] = &f76;
    jjtable[77] = &f77;
    jjtable[78] = &f78;
    jjtable[79] = &f79;
    jjtable[80] = &f80;
    jjtable[81] = &f81;
    jjtable[82] = &f82;
    jjtable[83] = &f83;
    jjtable[84] = &f84;
    jjtable[85] = &f85;
    jjtable[86] = &f86;
    jjtable[87] = &f87;
    jjtable[88] = &f88;
    jjtable[89] = &f89;
    jjtable[90] = &f90;
    jjtable[91] = &f91;
    jjtable[92] = &f92;
    jjtable[93] = &f93;
    jjtable[94] = &f94;
    jjtable[95] = &f95;
    jjtable[96] = &f96;
    jjtable[97] = &f97;
    jjtable[98] = &f98;
    jjtable[99] = &f99;
    jjtable[100] = &f100;    
    /*
    jjtable[101] = &f101;
    jjtable[102] = &f102;
    jjtable[103] = &f103;
    jjtable[104] = &f104;
    jjtable[105] = &f105;
    jjtable[106] = &f106;
    jjtable[107] = &f107;
    jjtable[108] = &f108;
    jjtable[109] = &f109;
    jjtable[110] = &f110;
    jjtable[111] = &f111;
    jjtable[112] = &f112;
    jjtable[113] = &f113;
    jjtable[114] = &f114;
    jjtable[115] = &f115;
    jjtable[116] = &f116;
    jjtable[117] = &f117;
    jjtable[118] = &f118;
    jjtable[119] = &f119;
    jjtable[120] = &f120;
    jjtable[121] = &f121;
    jjtable[122] = &f122;
    jjtable[123] = &f123;
    jjtable[124] = &f124;
    jjtable[125] = &f125;
    jjtable[126] = &f126;
    jjtable[127] = &f127;
    jjtable[128] = &f128;
    jjtable[129] = &f129;
    jjtable[130] = &f130;
    jjtable[131] = &f131;
    jjtable[132] = &f132;
    jjtable[133] = &f133;
    jjtable[134] = &f134;
    jjtable[135] = &f135;
    jjtable[136] = &f136;
    jjtable[137] = &f137;
    jjtable[138] = &f138;
    jjtable[139] = &f139;
    jjtable[140] = &f140;
    jjtable[141] = &f141;
    jjtable[142] = &f142;
    jjtable[143] = &f143;
    jjtable[144] = &f144;
    jjtable[145] = &f145;
    jjtable[146] = &f146;
    jjtable[147] = &f147;
    jjtable[148] = &f148;
    jjtable[149] = &f149;
    jjtable[150] = &f150;
    jjtable[151] = &f151;
    jjtable[152] = &f152;
    jjtable[153] = &f153;
    jjtable[154] = &f154;
    jjtable[155] = &f155;
    jjtable[156] = &f156;
    jjtable[157] = &f157;
    jjtable[158] = &f158;
    jjtable[159] = &f159;
    jjtable[160] = &f160;
    jjtable[161] = &f161;
    jjtable[162] = &f162;
    jjtable[163] = &f163;
    jjtable[164] = &f164;
    jjtable[165] = &f165;
    jjtable[166] = &f166;
    jjtable[167] = &f167;
    jjtable[168] = &f168;
    jjtable[169] = &f169;
    jjtable[170] = &f170;
    jjtable[171] = &f171;
    jjtable[172] = &f172;
    jjtable[173] = &f173;
    jjtable[174] = &f174;
    jjtable[175] = &f175;
    jjtable[176] = &f176;
    jjtable[177] = &f177;
    jjtable[178] = &f178;
    jjtable[179] = &f179;
    jjtable[180] = &f180;
    jjtable[181] = &f181;
    jjtable[182] = &f182;
    jjtable[183] = &f183;
    jjtable[184] = &f184;
    jjtable[185] = &f185;
    jjtable[186] = &f186;
    jjtable[187] = &f187;
    jjtable[188] = &f188;
    jjtable[189] = &f189;
    jjtable[190] = &f190;
    jjtable[191] = &f191;
    jjtable[192] = &f192;
    jjtable[193] = &f193;
    jjtable[194] = &f194;
    jjtable[195] = &f195;
    jjtable[196] = &f196;
    jjtable[197] = &f197;
    jjtable[198] = &f198;
    jjtable[199] = &f199;
    jjtable[200] = &f200;
    jjtable[201] = &f201;
    jjtable[202] = &f202;
    jjtable[203] = &f203;
    jjtable[204] = &f204;
    jjtable[205] = &f205;
    jjtable[206] = &f206;
    jjtable[207] = &f207;
    jjtable[208] = &f208;
    jjtable[209] = &f209;
    jjtable[210] = &f210;
    jjtable[211] = &f211;
    jjtable[212] = &f212;
    jjtable[213] = &f213;
    jjtable[214] = &f214;
    jjtable[215] = &f215;
    jjtable[216] = &f216;
    jjtable[217] = &f217;
    jjtable[218] = &f218;
    jjtable[219] = &f219;
    jjtable[220] = &f220;
    jjtable[221] = &f221;
    jjtable[222] = &f222;
    jjtable[223] = &f223;
    jjtable[224] = &f224;
    jjtable[225] = &f225;
    jjtable[226] = &f226;
    jjtable[227] = &f227;
    jjtable[228] = &f228;
    jjtable[229] = &f229;
    jjtable[230] = &f230;
    jjtable[231] = &f231;
    jjtable[232] = &f232;
    jjtable[233] = &f233;
    jjtable[234] = &f234;
    jjtable[235] = &f235;
    jjtable[236] = &f236;
    jjtable[237] = &f237;
    jjtable[238] = &f238;
    jjtable[239] = &f239;
    jjtable[240] = &f240;
    jjtable[241] = &f241;
    jjtable[242] = &f242;
    jjtable[243] = &f243;
    jjtable[244] = &f244;
    jjtable[245] = &f245;
    jjtable[246] = &f246;
    jjtable[247] = &f247;
    jjtable[248] = &f248;
    jjtable[249] = &f249;
    jjtable[250] = &f250;
    jjtable[251] = &f251;
    jjtable[252] = &f252;
    jjtable[253] = &f253;
    jjtable[254] = &f254;
    jjtable[255] = &f255;
    */
    
    //shuffle(jjtable, MAXX);

    int index=0;
    void (*foo)(unsigned char*, int, void* []) = jjtable[index];
    foo(newinput, index, jjtable);
}

int huge_raw_input(char* file_name){
  
  FILE *fp;
  fp = fopen(file_name, "r");
  unsigned char *input1 = malloc(MAXX + 1);
  fread(input1, MAXX, 1, fp);
  huge_branch(input1, MAXX); 
  fclose(fp); 
  
  return 0;
}
