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
 *	a_b_operation
 *	parameters: two unsigned ll ints and an int, which is the index in an array of strings, where each string is a predefined alias 
 *	for add or subtract or divide or multiply
 *	returns: void; prints the result of the operation on the two numbers when called. Prints "unknown error" if invalid value of op
 *	author: vkd
 *	last modified: 7th Sept. A.D. 2023
 */

//#define PRINT_TESTS

void
a_b_op
	(long int a, long int b, int op)
{
	if (op <= 4)
		printf
			("Your values have the sum %lli",
			(long long int) a + b);
	else if ((op - 4) <= 5)
		printf
            ("Your values have a difference %lli",
			(long long int) a - b);
	else if ((op - 9) <= 7)
		printf
			("Your values have a product %lli",
			(long long int) a * b);
	
	else if ((op - 16) <= 6) {
		double ratio = (double) a / b;
		printf
			("Your values have a ratio\n%.*f",
			precisionof(ratio), ratio);
		
		ratio = (double) b / a;
		printf
			("\nwhose reciprocal is\n%.*f",
			precisionof(ratio), ratio);
	}
	
	else
		printf
			("error");
	
	return;
}

int 
main(void) 
{

    char opn[100];
	/*Array of valid strings*/
	const char* operations[] =	
	{"add", "sum", "plus", "+", "minus", "difference", "subtract",
	"subtraction", "-", "product", "times", "into", "*", "x",
	"×", "multiply", "divide", "quotient", "by", "ratio", "/",
	"÷"};
    
	int i, valid = 0;
    
	char restart = 'y';
    
	long int num1, num2;
 
    while (restart == 'y' 
	|| restart == 'Y')
	{
		printf
			("Enter two positive numbers you wish to operate upon, in the form: a plus b\n");
		scanf
			(" %li %s %li",
			&num1, opn, &num2);

		for (i = 0; i < 22; i++) {
			if (strcmp(opn, operations[i]) == 0) {
				valid = i + 1;
				break;
			}
			else {
				#ifdef PRINT_TESTS
				printf
					("Not #%d: %s\n",
					i, operations[i]);
				#endif //PRINT_TESTS
			}
		}

		if (valid == 0) {
			printf
				("You did not enter a valid input for operation.");
		}

		else {
			a_b_op(num1, num2, valid);
		}
	
		printf
			("\nOnce more? y/n\n");
		scanf
			(" %c",
			&restart);
    }
	
	printf
		("Thank you for using the program!\n");
    
	return 0;

}