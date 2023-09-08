#include "./heads/useful.h"

int main(void) {

	char input[50];

	printf("Please enter the text you would like to print, in 50 characters or less\n");
	scanf("%s", input);
	
	printf("%s\n", input);

	return 0;

}