#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false)

using namespace std;

int main() {
  FastIO;
  int N;
  cin >> N;

  vector<int> memo(100001, 1e9);
  memo[0] = 0;
  vector<int> coins = {1, 2, 5, 7};
  for (const auto& coin : coins) {
    memo[coin] = 1;
  }

  for (int i = 3; i <= N; i++) {
    for (const auto& coin : coins) {
      int precoin = i - coin;
      if (precoin < 0) continue;
      memo[i] = min(memo[i], memo[precoin] + 1);
    }
  }
  cout << memo[N];

  return 0;
}