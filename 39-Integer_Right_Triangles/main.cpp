#include <iostream>

int main()
{
    int Max = 1000;
    int ans = 0;
    int maxCount = 0;

    for (int p = 1; p <= Max; p++)
    {
        int count = 0;
        for (int a = 2; a < p / 3; a++)
            for (int b = a; b < (p-a)/2; b++) // we iterate throw all the possible values of a and b
            {
                int c = p -a -b; // We force that c has the required value for the perimeter
                if ( c*c == a*a + b*b ) // If C also achives the pythagoras ecuation then it can be counted
                    count++;
            }
        
        // If I found a higher count for a parameter I remember it
        if (maxCount < count)
        {
            maxCount = count;
            ans = p;
        }
    }

    std::cout << ans << std::endl;

    return 0;
}