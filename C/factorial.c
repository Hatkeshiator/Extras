#include "./heads/useful.h"

/*
 *  factorial
 *  parameters: positive number
 *  returns: factorial of number
 *  author: vkd
 *  last modified: 19th Aug. A.D. 2023
 */
unsigned long long
factorial(unsigned long long a)
{
    unsigned long long i, f = 1;
    for (i = 2; i <= a; i++) {
        f *= i;
    }
    return f;
}

int
main(int argc, char* argv[])
{
    unsigned long long a = 0;
    
    printf
        ("Of which number to take factorial?\n");
    scanf
        ("%llu",
        &a);
    printf
        ("%llu! is %llu\n",
        a, factorial(a));
    return 0;
}