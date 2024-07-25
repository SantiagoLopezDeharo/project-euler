#include <iostream>
#include <cmath>
#include <vector>

// We define a function to know if a given number is prime or not
bool isprime(long long n)
{
    if (n == 2) return true;
    if (n%2 == 0) return false;
    for (long long i = 3; i <= sqrt(n); i+= 2)
        if (n % i == 0) return false;
    return true;
}


int main()
{
    long long n = 3;
    std::vector<long long> primes;
    primes.push_back(2);
    bool ok = false;
    while (true) // We iterate until we find it, since we know for certain that it exists
    {
        if (isprime(n)) primes.push_back(n); // If we find a prime number we add it to the vector of primes
        else // in case is not prime we check if it complis the conjecture
        {
            for (auto it = primes.begin(); it != primes.end() && !ok; it++ ) // we iterate to all prime numbers below n
                for (long long v = 1; v <= sqrt(n) && !ok; v++) // we iterate through all numbers below sqrt(n) since we are gonna square it
                    ok = ok || (n == (*it) + 2*v*v); // we check if it works
            if ( !ok )
            {
                std::cout << "The first odd number to fail the property is: " << n << std::endl; // we found one that it doesn't work
                return 0;
            }
        }
        ok = false;
        n += 2; // we iterate in sets of 2 to keep the odd property in n
    }
    return 0;
}