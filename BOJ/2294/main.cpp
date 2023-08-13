#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> coins;
    vector<int> dp(k + 1, 0);

    for (int i = 1; i <= n; i++) {
        int coin;
        cin >> coin;
        coins.push_back(coin);
    }
    sort(coins.begin(), coins.end());
    // unique(coins.begin(), coins.end());

    for (const auto &coin: coins) {
        for (int i = coin; i <= k; i++) {
            if (i % coin == 0) {
                dp[i] = i / coin;
            } else {
                if (dp[i - coin] == 0) {
                    continue;
                } else {
                    if (dp[i]) {
                        dp[i] = min(dp[i - coin] + 1, dp[i]);
                    } else {
                        dp[i] = dp[i - coin] + 1;
                    }
                }
            }
        }
    }

    if (dp[k] == 0) {
        cout << -1;
    } else {
        cout << dp[k];
    }
    return 0;
}
