#include "./heads/useful.h"
/*
 *  clearbuffer
 *  parameters: void
 *  returns: void (just clears input buffer)
 *  author: vkd
 *  last modified: 18th Aug. A.D. 2023
 */
void
clearbuffer(void)
{
	while (getchar() != '\n');
    return;
}

int
main(void)
{

    mpz_t a, b, sum;
    
    unsigned int i = 1, max;

    mpz_init(a); //GMP needs you to initialize variables before using them
    mpz_init(b);
    mpz_init(sum);

    mpz_set_ui(a, 1);
    mpz_set_ui(b, 1);

    printf
        ("\nUp to what (whichth?) fibonacci number do you want to check?\n");
    while(scanf("%u",&max) != 1) {
        printf
            ("Invalid input. Try again");
        clearbuffer();
    }

    while (i <= max) {
        printf
            ("%u.\t",
            i);
        gmp_printf("%Zd\n\n", a); //printf doesn't handle GMP no.s
        mpz_add(sum, a, b);
        mpz_set(a, b);  //a = b for GMP ints
        mpz_set(b, sum);
        i++;
    }
    //clear memory
    mpz_clear(a);
    mpz_clear(b);
    mpz_clear(sum);
    //it ran!
    return 0;
}