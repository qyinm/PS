#include <bits/stdc++.h>
#define FastIO cin.tie(NULL)->ios_base::sync_with_stdio(false);

using namespace std;
using pii = pair<int, int>;

bool dfs(int start, const pii* graph, int* match, bool* visited) {
  const auto& [from, to] = graph[start];
  for (int book = from; book <= to; book++) {
    if (visited[book]) continue;
    visited[book] = true;
    if (match[book] == -1 || dfs(match[book], graph, match, visited)) {
      match[book] = start;
      return true;
    }
  }

  return false;
}
void solve() {
  int n, m;
  cin >> n >> m;

  pii graph[1001];
  int match[1001];
  bool visited[1001];

  fill(match, match + 1001, -1);

  for (int i = 0; i < m; i++) {
    int from, to;
    cin >> from >> to;
    graph[i] = {from, to};
  }

  int cnt = 0;
  for (int i = 0; i < m; i++) {
    fill(visited, visited + 1001, false);
    if (dfs(i, graph, match, visited)) {
      cnt++;
    }
  }

  cout << cnt << "\n";
}

int main() {
  FastIO;

  int tc;
  cin >> tc;
  while (tc--) {
    solve();
  }

  return 0;
}