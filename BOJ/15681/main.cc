#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;
vector<bool> visited;
vector<vector<int>> graph;
vector<int> sizes;

int dfs(int curr) {
  visited[curr] = true;

  for (const auto& nxt : graph[curr]) {
    if (visited[nxt]) continue;
    sizes[curr] += dfs(nxt);
  }
  return sizes[curr];
}

int main() {
  FastIO;
  int N, R, Q;
  cin >> N >> R >> Q;

  visited.assign(N + 1, false);
  sizes.assign(N + 1, 1);
  graph.assign(N + 1, vector<int>());

  for (int i = 0; i < N - 1; i++) {
    int a, b;
    cin >> a >> b;
    graph[a].push_back(b);
    graph[b].push_back(a);
  }

  dfs(R);

  for (int q = 0; q < Q; q++) {
    int command;
    cin >> command;
    cout << sizes[command] << "\n";
  }
}