#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;
int N, M;
vector<vector<int>> graph;
vector<bool> visited;

void dfs(int curr, int cnt) {
  if (cnt == 5) {
    cout << "1";
    exit(0);
  }

  for (const auto& nxt : graph[curr]) {
    if (!visited[nxt]) {
      visited[nxt] = true;
      dfs(nxt, cnt + 1);
      visited[nxt] = false;
    }
  }
}

int main() {
  FastIO;
  cin >> N >> M;
  graph.assign(N, vector<int>());

  for (int i = 0; i < M; i++) {
    int a, b;
    cin >> a >> b;
    graph[a].push_back(b);
    graph[b].push_back(a);
  }

  for (int i = 0; i < N; i++) {
    visited.assign(N, false);
    visited[i] = true;
    dfs(i, 1);
  }
  cout << 0;

  return 0;
}