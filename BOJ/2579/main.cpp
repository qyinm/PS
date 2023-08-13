#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    int arr[301]{0,};
    int dp[301]{0, };
    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
    }
    dp[1] = arr[1];
    if (n > 1) {
        dp[2] = arr[2] + arr[1];
    }
    for (int i = 3; i <= n; i++) {
        dp[i] = arr[i] + max(dp[i - 2], arr[i - 1] + dp[i - 3]);
    }

    cout << dp[n];
    return 0;
}
