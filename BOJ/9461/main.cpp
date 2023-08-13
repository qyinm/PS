#include <iostream>

using namespace std;

int main() {
    long long dp[101] = {0, 1, 1, 1};
    int n;
    cin >> n;


    for (int i = 4; i <= 100; i++) {
        dp[i] = dp[i - 2] + dp[i - 3];
    }

    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        cout << dp[temp] << "\n";
    }
    return 0;
}
