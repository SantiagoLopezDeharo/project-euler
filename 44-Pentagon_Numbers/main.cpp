#include <iostream>
#include <cmath>
#include <vector>

bool isPentagonal(long x) {
    double n = (1 + sqrt(1 + 24 * x)) / 6;
    return n == (long) n;
}

long pentagonal(int n) {
    return n * (3LL * n - 1) / 2;
}

int main() {
    std::vector<long> pentagonals;
    int n = 1;

    while (true) {
        long P_n = pentagonal(n);
        pentagonals.push_back(P_n);

        for (auto P_j : pentagonals) {
            if (P_j == P_n) continue;
            long P_k = P_n;
            if (isPentagonal(P_k - P_j) && isPentagonal(P_k + P_j)) {
                std::cout << "D = " << P_k - P_j << std::endl;
                return 0;
            }
        }

        n++;
    }

    return 0;
}
