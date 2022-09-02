#include <iostream>

using namespace std;

int main() {
    int n;
    int arr[1001] = {
        0,
    };
    int dp[1001] = {
        0,
    };
    int mmax = -1;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        int tmp;
        cin >> tmp;
        arr[i] = tmp;
        if (dp[tmp] == 0) {
            dp[tmp] = 1;
        }
        int m = 0;
        for (int j = 1; j < tmp; j++) {
            if (dp[j] != 0 && dp[j] > m) {
                m = dp[j];
            }
        }

        dp[tmp] = max(dp[tmp], m + 1);

        if (dp[tmp] > mmax) {
            mmax = dp[tmp];
        }
    }
    cout << mmax;
    return 0;
}
