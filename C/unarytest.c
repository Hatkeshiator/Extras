#include "./heads/useful.h"



int main(void) {
    int a, b;

    printf
        ("Initial value of a = ");
    scanf
        ("%d", &a);
    a++;
    printf
        ("\nIf a++;\na = %d",
        a);
    a--;
    b = a++;
    printf
        ("\nIf b = a++;\na = %d\nb = %d",
        a, b);
    a--;
    b = ++a;
    printf
        ("\nIf b = ++a;\na = %d\nb = %d",
        a, b);
    a--;
    b = ++a;
    a--;
    printf
        ("\nIf b = ++a; a--;\na = %d\nb = %d\n",
        a, b);

    return 0;
}