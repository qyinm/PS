#include <iostream>
#include <cmath>

using namespace std;

long long int first = 1, second = 1;
long long int mod = 1000000007;

int dividesFunc(int k) {
    if (k == 0) {
        return 1;
    }

    if (k % 2 == 1) {
        return (second * dividesFunc(k - 1)) % mod;
    } else {
        long long int half = dividesFunc(k / 2);
        return half * half % mod;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);


    long long int n, k;
    cin >> n >> k;

    for (int i = n; i > n - k; i--) {
        first = (first * i) % mod;
    }

    for (int i = 1; i <= k; i++) {
        second = (second * i) % mod;
    }

    second = dividesFunc(mod - 2);
    cout << (first* second) % mod << endl;

    return 0;
}