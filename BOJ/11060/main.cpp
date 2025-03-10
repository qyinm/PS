#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;

int main() {
  FastIO;
  int N;
  cin >> N;

  vector<int> steps(N);
  for (auto& step : steps) {
    cin >> step;
  }
  vector<int> memo(N, 1e9);
  memo[0] = 0;
  for (int i = 0; i < N; i++) {
    if (i != 0 && memo[i] == 0) continue;
    for (int s = 1; s <= steps[i] && i + s < N; s++) {
      memo[i + s] = min(memo[i + s], memo[i] + 1);
    }
  }
  if (memo[N - 1] == 1e9) {
    cout << -1;
    return 0;
  }
  cout << memo[N - 1];
  return 0;
}