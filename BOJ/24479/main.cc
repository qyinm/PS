#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;
vector<vector<int>> graph;
vector<int> visited;

void dfs(int curr, int& cnt) {
  visited[curr] = cnt;

  for (const auto& nxt : graph[curr]) {
    if (visited[nxt] != 0) continue;
    cnt++;
    dfs(nxt, cnt);
  }
}

int main() {
  FastIO;

  int N, M, R;
  cin >> N >> M >> R;

  graph.assign(N + 1, vector<int>());
  visited.assign(N + 1, 0);

  for (int i = 0; i < M; i++) {
    int a, b;
    cin >> a >> b;
    graph[a].push_back(b);
    graph[b].push_back(a);
  }
  for (auto& g : graph) {
    sort(g.begin(), g.end());
  }

  int cnt = 1;
  dfs(R, cnt);

  for (int i = 1; i <= N; i++) {
    cout << visited[i] << "\n";
  }

  return 0;
}