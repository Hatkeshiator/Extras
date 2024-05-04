#include "./heads/useful.h"

/*
 *  lowestfactor
 *  parameter: number whose lowest factor you want to find
 *  returns: 
 *      0: number is not valid
 *      n: lowest factor of the number not including 1
 *  author: vkd
 *  last modified: 23rd Aug. A.D. 2023
 */

unsigned long long
lowestfactor(unsigned long long a)
{
	unsigned long long i = 0, r = a;
    
    //indicates invalid input
	if (a <= 1) {
		r = 0;
	}
    //handle even numbers first to reduce load on function proper 
	else if (a % 2 == 0) {
		r = 2;
	}
	//similarly,
	else if (a % 3 == 0) {
		r = 3;
	} else if (a % 5 == 0) {
		r = 5;
	}
    
    //run through all odd numbers and set our factor to the smallest one we encounter by which the given number is divisible
	else {
		for (i = 3; i <= sqrt(a); i += 2) {
			if (a % i == 0) {
				r = i;
				break;
			}
		}
	}

    //return the factor
	return r;
}

/*
 *  factorize
 *  parameter: number to be factorized
 *  returns:
 *      if prime: is prime
 *      if composite: is composite + list of factors
 *      "something terrible..." error message: lowestfactor <= 1 which is not possible according to lowestfactor function
 *  author: vkd
 *  last modified: 18th Aug. A.D. 2023
 */

void
factorize(unsigned long long a)
{
	unsigned long long prime = lowestfactor(a);
    
    //indicates prime value
	if (prime == a) {
		printf
			("The number %llu is prime\n", a);
	}
	
    //indicates factors other than 1 and itself
	else if (prime > 1) {
		unsigned long long i = 0;

		printf
		    ("The number %llu is a composite number\nThe complete factorization of your number is:\n\n",
		     a);

		while ((i = lowestfactor(a)) > 1) {
			printf("%llu\tdivided by\t%llu\tis\t", a, i);
			a /= i;
			printf("%llu\n", a);
		}

		printf("\n");
	}
    
    //indicates error as lowestfactor <= 1 which we did not allow for
    else {
		printf
		    ("Something terrible has happened. Sorry. Please run the program again\n");
	}
	return;
}

/*
 *  clearbuffer
 *  parameters: void
 *	returns: void (just clears input buffer)
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
main(int argc, char *argv[])
{
	printf
		("\n");
    
    //if passed without args, ask user what they want to input
	if (argc == 1) {
		unsigned long long tocheck = 0, prime = 0;

		printf
		    ("Enter the number you wish to check\n(strictly 0 < [value] < %llu): ",
		     ULLONG_MAX);

		while (scanf(" %llu", &tocheck) != 1) {
			printf
			    ("Enter a value such that:\n0 < value < %llu\n",
			     ULLONG_MAX);
			clearbuffer();

		}

		while (tocheck <= 1) {
			printf
			    ("Enter a value such that:\n0 < value < %llu\n",
				ULLONG_MAX);
        	
			while (scanf(" %llu", &tocheck) != 1) {
				printf
				    ("Enter a value such that:\n0 < value < %llu\n",
					ULLONG_MAX);
				clearbuffer();
			}

			clearbuffer();
		}

		factorize(tocheck);
	}
    
    //if command line args are passed, factorize each space-separated number separately
	else {

		for (int i = 1; i < argc; i++) {

			unsigned long long tocheck =
              strtoull(argv[i], NULL, 10), prime = 0;
        
			if (tocheck <= 1) {
				printf
				    ("Invalid input or other error. Skipping %s.\n\n\a",
				     argv[i]);
			}
    

			else {
				factorize(tocheck);
			}
		}
	}

	return 0;
}