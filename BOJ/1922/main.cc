#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;

vector<int> parents;
int N, M;

int find(int i) {
  if (parents[i] < 0) return i;
  return parents[i] = find(parents[i]);
}

bool unions(int i, int j) {
  i = find(i);
  j = find(j);
  if (i == j) return false;
  if (parents[i] < parents[j]) {
    parents[i] += parents[j];
    parents[j] = i;
  } else {
    parents[j] += parents[i];
    parents[i] = j;
  }
  return true;
}

int main() {
  FastIO;
  cin >> N >> M;

  vector<tuple<int, int, int>> edges;
  parents = vector<int>(N + 1, -1);
  for (int i = 0; i < M; i++) {
    int a, b, c;
    cin >> a >> b >> c;
    edges.push_back({c, a, b});
  }
  sort(edges.begin(), edges.end());
  int ans = 0;
  for (const auto& [cost, a, b] : edges) {
    if (!unions(a, b)) continue;
    ans += cost;
  }
  cout << ans;

  return 0;
}