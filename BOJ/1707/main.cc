#include <bits/stdc++.h>
#define FastIO cin.tie(NULL)->ios_base::sync_with_stdio(false);

using namespace std;

vector<vector<int>> graph;
vector<int> colors;

bool dfs(int current, int color) {
  colors[current] = color;

  for (const auto& next : graph[current]) {
    if (colors[next] == 0) {
      if (!dfs(next, -color)) {
        return false;
      }
    } else if (colors[next] == color) {
      return false;
    }
  }
  return true;
}

void solve() {
  int v, e;
  cin >> v >> e;

  graph = vector<vector<int>>(v + 1);
  colors = vector<int>(v + 1, 0);
  for (int i = 0; i < e; i++) {
    int a, b;
    cin >> a >> b;
    graph[a].push_back(b);
    graph[b].push_back(a);
  }

  for (int i = 1; i <= v; i++) {
    if (colors[i] != 0) continue;
    if (!dfs(i, 1)) {
      cout << "NO\n";
      return;
    }
  }
  cout << "YES\n";
  return;
}

int main() {
  FastIO;

  int tc;
  cin >> tc;

  while (tc--) {
    solve();
  }
}