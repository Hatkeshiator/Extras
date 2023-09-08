#include "./heads/useful.h"

/*
 *  reversestring
 *  parameters: string
 *  returns: void (prints the string with letters in reverse order)
 *  author: vkd
 *  last modified: 30/8/23
 */

void
reversestring(char a[])
{
    int length = 0;

    while(a[length] != '\0') ++length; 

    char output[length]; //reverse of the string has the same length as itself forwards
    int chars_put;

    for(chars_put = 0; chars_put < length; chars_put++) output[chars_put] = a[length - chars_put - 1]; //output = input backwards

    output[length] = '\0'; //if final letter != null, undefined behaviour results

    printf("%s ", output);

    return;
}


int
main(int argc, char *argv[])
{
    int i;

    printf("\n");

    for (i = 1; i < argc; i++) reversestring(argv[i]);
    printf("\n\n");

    return 0;
}