#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h> 

//#define DEBUG
#define MAX 256


#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h> 

int rem(int retval, int group){
  printf("ren\n");
  return (unsigned int)retval % group;
}

int markfunc(int a){
  return 0;
}

int dummy2(int a){
  return 0;
}

void dummy(int a, int b, int c, int d){
  __asm__ (
    "nop\n"
    "nop\n"
    "nop"
  ); 
}

