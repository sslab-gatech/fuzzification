#include <stdio.h>
#include <stdlib.h>

unsigned reverse(unsigned x) {
   x = ((x & 0x55555555) <<  1) | ((x >>  1) & 0x55555555);
   x = ((x & 0x33333333) <<  2) | ((x >>  2) & 0x33333333);
   x = ((x & 0x0F0F0F0F) <<  4) | ((x >>  4) & 0x0F0F0F0F);
   x = (x << 24) | ((x & 0xFF00) << 8) |
       ((x >> 8) & 0xFF00) | (x >> 24);
   return x;
}

unsigned int crc32(unsigned char *message) {
   int i, j;
   unsigned int byte, crc;

   i = 0;
   crc = 0xFFFFFFFF;
   while (message[i] != 0) {
      byte = message[i];            // Get next byte.
      byte = reverse(byte);         // 32-bit reversal.
      for (j = 0; j <= 7; j++) {    // Do eight times.
	         if ((int)(crc ^ byte) < 0)
              crc = (crc << 1) ^ 0x04C11DB7;
         else crc = crc << 1;
         byte = byte << 1;          // Ready next msg bit.
      }
      i = i + 1;
   }
   return reverse(~crc);
}

int modifyInt(int in) { //no overloading in C  
	char buffer [200];	
	sprintf(buffer, "%d", in + 100000);
	int crc = (int)crc32(buffer);
	int diff = crc - in;  	
	return crc - diff;
} 
double modifyDouble(double in) {
	char buffer [200];
	sprintf(buffer, "%lf", in + 100000.0);
	double crc = (double)crc32(buffer);
	double diff = crc - in;
	return crc - diff;
}

float modifyFloat(float in) {
  char buffer [200];
	sprintf(buffer, "%f", in + 100000.0);
	float crc = (float)crc32(buffer);
	float diff = crc - in;
	return crc - diff;
}

/*
char modifyBool(char a) { //for c++ bools since they are represented as i8 ints in IR
  printf("anti-symb bool function here - operand: %d \n",a);
  return a | 0;
}
*/

// for now, we are just using the same wrapper function above
int retWrapInt(int in){
  char buffer [200];	
	sprintf(buffer, "%d", in + 100000);
	int crc = (int)crc32(buffer);
	int diff = crc - in;  	
	return crc - diff;
}
double retWrapDouble(double in){
	char buffer [200];
	sprintf(buffer, "%lf", in + 100000.0);
	double crc = (double)crc32(buffer);
	double diff = crc - in;
	return crc - diff;
}
float retWrapFloat(float in){
  char buffer [200];
	sprintf(buffer, "%f", in + 100000.0);
	float crc = (float)crc32(buffer);
	float diff = crc - in;
	return crc - diff;
}
