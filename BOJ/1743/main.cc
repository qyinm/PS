#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;

int N, M, K;
vector<vector<int>> graph;
vector<vector<bool>> visited;
pair<int, int> weights[4] = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};

int dfs(int y, int x) {
  visited[y][x] = true;

  int cnt = 1;
  for (const auto& [wy, wx] : weights) {
    int ny = y + wy;
    int nx = x + wx;
    if (ny < 1 || ny > N || nx < 1 || nx > M) continue;
    if (visited[ny][nx]) continue;
    if (graph[ny][nx] != 1) continue;
    int df = dfs(ny, nx);
    cnt += df;
  }

  return cnt;
}

int main() {
  FastIO;
  cin >> N >> M >> K;
  graph.assign(N + 1, vector<int>(M + 1, 0));

  vector<pair<int, int>> garbages(K);
  for (int i = 0; i < K; i++) {
    int r, c;
    cin >> r >> c;
    graph[r][c] = 1;
    garbages[i] = {r, c};
  }

  int ans = -1;
  visited.assign(N + 1, vector<bool>(M + 1));
  for (const auto& [r, c] : garbages) {
    if (visited[r][c]) continue;

    ans = max(ans, dfs(r, c));
  }

  cout << ans;

  return 0;
}