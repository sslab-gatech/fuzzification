#include <unistd.h>

int modifyInt(int in) { //no overloading in C  	
	usleep(20000);
	return in;
} 
double modifyDouble(double in) {
	usleep(20000);	
	return in;
}

float modifyFloat(float in) {
	usleep(20000);
  	return in;
}

// for now, we are just using the same wrapper function above
int retWrapInt(int in){
	usleep(20000);
	return in;
}
double retWrapDouble(double in){
	usleep(20000);
	return in;
}
float retWrapFloat(float in){
	usleep(20000);
	return in;
}
