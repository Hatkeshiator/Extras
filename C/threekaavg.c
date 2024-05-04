#include "./heads/useful.h"

double avgthr(int a, int b, int c) {
	double avg;

	avg = (double) (a + b + c) / 3;

	return avg;
}
int main(void) {
	int a, b, c;

	printf
		("Please enter three numbers to take the average of.\n");
	scanf
		(" %d %d %d",
		&a, &b, &c);

	printf
		("\nThe mean of %d, %d, and %d is %f\n",
		a, b, c,
		avgthr(a, b, c));
	
	return 0;
}