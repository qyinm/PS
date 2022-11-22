#include <iostream>
#include <vector>
using namespace std;

int main() {
    cin.tie(0);
    int n, q;
    vector<vector<int>> arr(1025, vector<int>(1025, 0));
    vector<vector<int>> dp(1025, vector<int>(1025, 0));

    cin >> n >> q;

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            cin >> arr[i][j];
        }
    }
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            dp[i][j] = arr[i][j] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1];
        }
    }

    for (int i = 0; i < q; ++i) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        cout << dp[x2][y2] - dp[x2 ][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1] << "\n";
    }

    return 0;
}
