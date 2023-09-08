#include "./heads/useful.h"

/*
 *  vowelcount
 *  parameters: a string
 *  returns: the number of vowels (letters equal to one of: a, e, i, o, u, A, ..., U) in the string
 *  author: vkd
 *  last modified: 30th August, 2023
 */

int
vowelcount(char tocount[])
{
    int i, vowcount = 0;

    char letter;
    //check each letter of the string and tally up the vowels
    for (i = 0; i < strlen(tocount); i++) {
        letter = tolower(tocount[i]);
        if (letter == 'a'
            || letter == 'e'
            || letter == 'i'
            || letter == 'o'
            || letter == 'u') 
        {
            vowcount++;
        }
    }
    return vowcount;
}

int
main(int argc, char *argv[])
{
    int i;

    printf
        ("Calculating...\n\n");
    //treat each argument as a separate word and calculate vowel count for each
    for(i = 1; i < argc; i++) {
        printf
            ("The number of vowels in word no. %d\t(%s)\t\tis\t%d...\n\n",
            i, argv[i], vowelcount(argv[i]));
    }
    printf
        ("I hope you had fun.\n");

    return 0;
}