#include <iostream>
#include <cmath>

/*

Explanation:

We need to find Tn = Pm = Hv

If we force this to happen, we will get to: 
    3.m^2 - m - n(n+1) = 0 
    4v^2 -2v - n(n+1) = 0

so we can deduct that:
    m = (1 + sqrt(1 + 4*3*n(n+1))) / 6
    v = (2 + sqrt(4 + 4*4*n(n+1))) / 8

we can forget abour the case in which we rest the sqrt since it would always be negative

so now we only have to iterate through all n's after 285 until we find one that has a m and v that are integers

*/


long long T(long long n)
{
    return n*(n+1) / 2;
}

long long P(long long n)
{
    return n*(3*n - 1) / 2;
}

long long H(long long n)
{
    return n*(2*n - 1);
}

long long getP(long long n)
{
    double m = (1 + sqrt( 1 + 12*n*(n+1) ))/6;
    if ( m == (long long) m ) return (long long) m;
    
    return -1;
}

long long getH (long long n)
{
    double v = (2 + sqrt( 4 + 16*n*(n+1) ))/8;
    if ( v == (long long) v ) return (long long) v;
    
    return -1;
}

int main()
{
    long long n = 286;

    while (true)
    {
        long long m = getP(n);
        long long v = getH(n);
        if ( (m != -1) && (v != -1) )
        {
            long long Tn = T(n);
            long long Pm = P(m);
            long long Hv = H(v);

            if ( (Tn == Pm) && (Pm == Hv) )
            {
                std::cout << "The next triangle number is: " << Tn << std::endl;
                return 0;
            }
            
        }
        n++;
    }
    return 0;
}