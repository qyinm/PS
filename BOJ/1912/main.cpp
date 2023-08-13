#include<iostream>
#include<vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> vec(n);
    vector<int> dp(n, -1e9);
    for (auto& v: vec) {
        cin >> v;
    }

    int ans = -1e9;
    for (int i = n-1; i >= 0; i--) {
        dp[i] = vec[i];
        if (i != n-1) {
            dp[i] = max(dp[i], vec[i] + dp[i+1]);
        }
        ans = max(ans, dp[i]);
    }
    cout << ans << endl;
    
}