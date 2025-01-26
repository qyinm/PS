#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;

vector<vector<int>> graph;
pair<int, int> weights[] = {{1, 0}, {0, 1}, {0, -1}, {-1, 0}};
int N;

int dijkstra() {
  priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>,
                 greater<tuple<int, int, int>>>
      pq;
  vector<vector<int>> distances(N, vector<int>(N, 1e9));
  pq.push({0, 0, 0});
  distances[0][0] = 0;

  while (!pq.empty()) {
    auto [cost, y, x] = pq.top();
    pq.pop();
    // cout << "cost: " << cost << " y: " << y << " x: " << x << endl;

    if (y == N - 1 && x == N - 1) return cost;

    for (const auto& [wy, wx] : weights) {
      int ny = y + wy;
      int nx = x + wx;

      if (ny < 0 || ny >= N || nx < 0 || nx >= N) continue;
      int ncost = cost + (graph[ny][nx] == 1 ? 0 : 1);
      if (distances[ny][nx] > ncost) {
        distances[ny][nx] = ncost;
        pq.push({ncost, ny, nx});
      }
    }
  }

  return distances[N - 1][N - 1];
}

int main() {
  FastIO;
  cin >> N;
  graph.assign(N, vector<int>(N));

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      char c;
      cin >> c;
      graph[i][j] = (c - '0');
    }
  }
  cout << dijkstra();

  return 0;
}