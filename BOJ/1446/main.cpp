#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false)

using namespace std;
using pi = pair<int, int>;

int main() {
  FastIO;
  int N, D;
  cin >> N >> D;

  map<int, vector<pi>> m;
  int from, to, cost;
  for (int i = 0; i < N; i++) {
    cin >> from >> to >> cost;
    m[from].push_back({to, cost});
  }

  vector<int> memo(D + 1, 987654321);

  memo[0] = 0;
  for (int i = 0; i < D; i++) {
    if (m.find(i) != m.end()) {
      for (const auto& [to, cost] : m[i]) {
        memo[to] = min(memo[to], memo[i] + cost);
      }
    }
    memo[i + 1] = min(memo[i + 1], memo[i] + 1);
  }
  cout << memo[D];

  return 0;
}