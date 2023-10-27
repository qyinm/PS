#include <iostream>
#include <cstring>
#define MOD 1000000009

using namespace std;

long long int cache[100001][4];


long long int top(long long int idx, long long int last) {
    
    long long int &ref = cache[idx][last];
    if (idx <= 3 || ref != 0) {
        return ref;
    }

    for (int i = 1; i < 4; i++) {
        if (last != i) {
            ref += top(idx - last, i) % MOD;
        }
    }
    return ref % MOD;
}

int main()
{
    cache[1][1] = 1;
    cache[2][2] = 1;
    cache[3][1] = 1;
    cache[3][2] = 1;
    cache[3][3] = 1;
    
    int t;
    cin >> t;
    for (; t > 0; t--) {
        int n;
        cin >> n;
        
        cout << (top(n, 1) + top(n, 2) + top(n, 3)) % MOD << "\n";
    }

    return 0;
}
