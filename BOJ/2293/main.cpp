#include <iostream>

using namespace std;
int dp[10001];
int data[101];
int main() {
    int n, k;

    cin >> n >> k;
    for (int i = 1; i <= n; i++) {
        cin >> data[i];
    }
    dp[0] = 1;
    for (int i = 1; i <= n; i++) {
        for (int j = data[i]; j <= k; j++) {

            dp[j] = dp[j - data[i]] + dp[j];

        }
    }
    cout << dp[k];
    return 0;
}
