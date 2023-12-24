#include <stdio.h>
#include <cmath>

int Cdivisores(int a) 
{
    int d = 0;
    for (int i = 0; i < sqrt(a); i++) {
        if (a % (i + 1) == 0) {
            d += 2;
        }
    }
    return d;
}

int main() 
{
    int div = 0;
    int divisores = 500;
    int n = 1;

    while (div <= divisores) {
        int a = n * (n + 1) / 2;
        div = Cdivisores(a);
        n = n + 1;
    }

    printf("%d \n",(n - 1) * n / 2);

    return 0;
}