/*
gcc -c test.c 
gcc -o out test.o delay_1.o
*/
#include <stdio.h>
#include <time.h>
#include <unistd.h>
#include "csmith.h"

int global1;
int global2;

void main(){
  struct timespec start, stop;
  clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &start);
  slp(0);
  //usleep(1000);
  clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &stop);
  double result = (stop.tv_sec - start.tv_sec) / 1000  + (stop.tv_nsec - start.tv_nsec) / 1e6;    // in microseconds

  
  printf("%f\n", result);
}
