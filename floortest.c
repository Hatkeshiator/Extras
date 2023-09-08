#include "./heads/useful.h"

/*
 *	precisionof
 *	parameters: double
 *	returns: int value of number of places after the decimal point after which trailing zeroes start.
 *	author: vkd
 *	last modified: 7th Sept. A.D. 2023
 */

int
precisionof(double a)
{
	int precision = 0;
	while(fmod(a * pow(10, precision), 1) != 0)
		precision++;
	return precision;
}

/*
 *  floorswap
 *  parameters: two pointers
 *  returns: void; sets *x to floor(*y) and *y to floor(*x)
 *  author: vkd
 *  last modified: 8th Sept. A.D. 2023
 */

void
floorswap(double* x, double* y)
{
    double a = *x;
    *x = *y;
    *y = a;
    return;
}

int main(void) {

    double x, y;

    printf
        ("Please enter TWO (2) values\n");
    scanf
        (" %lf %lf",
        &x, &y);
    
    printf
        ("\nThe values are %.*lf, %.*lf\n",
        precisionof(x), x, precisionof(y), y);
    floorswap(&x, &y);
    printf("\nThe values are %.1lf, %.1lf after swapping their floor values\n", x, y);

    return 0;

}