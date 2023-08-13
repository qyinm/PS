#include <iostream>

using namespace std;

int main() {
    int c;
    int dp[2][100001]{0, };
    int arr[2][100001]{0, };
    cin >> c;
    for (int i = 0; i < c; i++) {
        int n;
        cin >> n;
        int m = 0;
        for (auto &j: arr) {
            for (int k = 1; k <= n; k++) {
                cin >> j[k];
            }
        }
        dp[0][1] = arr[0][1];
        dp[1][1] = arr[1][1];
        for (int k = 2; k <= n; k++) {
            dp[0][k] = arr[0][k] + max(dp[1][k - 2], dp[1][k - 1]);
            dp[1][k] = arr[1][k] + max(dp[0][k - 2], dp[0][k - 1]);

        }
        cout << max(dp[0][n], dp[1][n]) << "\n";
    }

    return 0;
}
