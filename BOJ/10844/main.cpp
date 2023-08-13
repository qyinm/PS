#include <iostream>
#include <vector>

using namespace std;

int main() {
    int dp[101][10] = {{0,},
                       {0, 1, 1, 1, 1, 1, 1, 1, 1, 1}};
    int n;
    cin >> n;
    for (int i = 2; i <= n; ++i) {
        dp[i][0] = dp[i - 1][1] % 1000000000;
        for (int j = 1; j < 9; ++j) {
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % 1000000000;
        }
        dp[i][9] = dp[i - 1][8] % 1000000000;
    }
    long long ans = 0;
    for (int i = 0; i < 10; i++) {
        ans += dp[n][i];
    }
    cout << ans % 1000000000;
    return 0;
}
