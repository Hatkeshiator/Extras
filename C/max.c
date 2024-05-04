#include "./heads/useful.h"

int
main(void)
{
    int a, b, max;

    char keepgoing = 'y';

    printf
        ("Enter any two numbers.\n");
    scanf
        (" %d %d",
        &a, &b);
    while(keepgoing == 'y'
        || keepgoing == 'Y') {
       
        if (a == b) { 
            printf
                ("The number and the maximum so far are equal.");
        }
        else {
            max = ((a > b) ? a : b);
            printf
                ("The bigger number of the last two is %d",
                max); 
        }
       
        printf
            ("\nKeep going? y/n");
        scanf
            (" %c", &keepgoing);
       
        if (keepgoing == 'y'
            || keepgoing == 'Y') {
            printf
                ("\nEnter another number: ");
            scanf
                (" %d", &a);
        }
    }

    return 0;
}