#include <iostream>
#include <vector>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;

int n;
vector<int> L;
vector<int> J;
int dp(int i, int health, vector<vector<int>>& cache) {
  if (health <= 0) {
    return -1e9;
  }
  if (i == n) {
    return 0;
  }
  if (cache[i][health] != -1) {
    return cache[i][health];
  }
  cache[i][health] = 0;
  return cache[i][health] = max(dp(i + 1, health, cache),
                                dp(i + 1, health - L[i], cache) + J[i]);
}

int main() {
  FastIO;
  cin >> n;
  L.resize(n);
  J.resize(n);
  for (auto& l : L) {
    cin >> l;
  }
  for (auto& j : J) {
    cin >> j;
  }
  vector<vector<int>> cache(n, vector<int>(101, -1));
  cout << dp(0, 100, cache);
  return 0;
}