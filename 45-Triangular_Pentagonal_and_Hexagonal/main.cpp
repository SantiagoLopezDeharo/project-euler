#include <iostream>
#include <cmath>

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