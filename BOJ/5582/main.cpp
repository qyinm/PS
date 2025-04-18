#include <bits/stdc++.h>

using namespace std;

string s1, s2;
vector<vector<int>> memo;
int ans = 0;

int dp(int i, int j) {
  if (i < 0 || j < 0) return 0;

  if (memo[i][j] != -1) return memo[i][j];

  if (s2[i] == s1[j]) {
    memo[i][j] = dp(i - 1, j - 1) + 1;
    ans = max(ans, memo[i][j]);
  } else {
    memo[i][j] = 0;
  }

  return memo[i][j];
}

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  cin >> s1 >> s2;

  int n = s2.length(), m = s1.length();
  memo.assign(n, vector<int>(m, -1));

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      dp(i, j);
    }
  }

  cout << ans;
  return 0;
}
