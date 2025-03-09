#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false)

using namespace std;

int main() {
  FastIO;
  int n;
  cin >> n;
  vector<int> memo(n + 1);
  for (int i = 2; i <= n; i++) {
    for (int j = 1; j <= i / 2; j++) {
      memo[i] = max(memo[i], (j * (i - j) + memo[j] + memo[i - j]));
    }
  }
  cout << memo[n];
  return 0;
}