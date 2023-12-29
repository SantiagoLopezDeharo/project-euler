#include <stdio.h>
#include <unordered_set>

using namespace std;

bool belongs(unordered_set<unsigned int> set, unsigned int a)
{
    if (set.find(a) != set.end())
        return true;

    return false;
}

// I create a function that calculates the size of the cycle of a fraction, if there is no cycle it returns -1

unsigned int cycle_size(int a, int b)
{
    unordered_set<unsigned int> restos;
    bool cycle = false;
    unsigned int cycle_s = 0;
    while(a < b)
        a *= 10;
    while (!cycle && (a != 0))
    {
        while(a < b)
        {
            a *= 10;
            cycle_s++;
        }
        a = a % b;
        a *= 10;
        if (belongs(restos, a))
            cycle = true;
        restos.insert(a);
        cycle_s++;
    }
    if (cycle) return cycle_s;

    restos.clear();
    return -1;
}

int main()
{
    int dm = 1000;
    int max = -1;
    int aux = 0;
    for (int d = 1; d < dm; d++)
    {
        aux = cycle_size(1, d);
        if (aux > max)
            max = aux;
    }
    printf("The maximum cycle size was: %d \n", max);
    return 0;
}