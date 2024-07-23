#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

long long ans = 0;

using namespace std;

// Function to check if the number has the required properties
bool property(const string& n) {
    vector<string> digits = {
        n.substr(1, 3), 
        n.substr(2, 3),
        n.substr(3, 3),
        n.substr(4, 3),
        n.substr(5, 3),
        n.substr(6, 3),
        n.substr(7, 3)
    };
    
    return (stoi(digits[0]) % 2 == 0) && 
           (stoi(digits[1]) % 3 == 0) && 
           (stoi(digits[2]) % 5 == 0) && 
           (stoi(digits[3]) % 7 == 0) && 
           (stoi(digits[4]) % 11 == 0) && 
           (stoi(digits[5]) % 13 == 0) && 
           (stoi(digits[6]) % 17 == 0);
}

// Function to calculate the answer by checking all permutations
void calculate_ans() {
    string s = "0123456789";
    do {
        if (property(s)) {
            ans += stoll(s);
        }
    } while (next_permutation(s.begin(), s.end()));
}

int main() {
    calculate_ans();
    cout << ans << endl;
    return 0;
}
