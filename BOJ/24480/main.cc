#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;
int N, M, R, cnt;
vector<vector<int>> graph;
vector<int> visited;

void dfs(int curr) {
  visited[curr] = ++cnt;

  for (const auto& nxt : graph[curr]) {
    if (visited[nxt] != 0) continue;
    dfs(nxt);
  }
}

int main() {
  FastIO;
  cin >> N >> M >> R;

  graph.assign(N + 1, vector<int>());
  for (int i = 0; i < M; i++) {
    int a, b;
    cin >> a >> b;

    graph[a].push_back(b);
    graph[b].push_back(a);
  }

  for (int i = 1; i <= N; i++) {
    sort(graph[i].begin(), graph[i].end(), [](int a, int b) { return a > b; });
  }
  visited.assign(N + 1, 0);

  dfs(R);
  for (int i = 1; i <= N; i++) {
    cout << visited[i] << "\n";
  }

  return 0;
}