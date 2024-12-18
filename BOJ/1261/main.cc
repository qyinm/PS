#include <iostream>
#include <queue>
#include <vector>

using namespace std;
using ll = long long;
using pii = pair<int, int>;

vector<pii> weights = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

int dijkstra(const vector<vector<int>>& graph, const int& n, const int& m) {
  priority_queue<pair<ll, pii>, vector<pair<ll, pii>>, greater<>> pq;
  vector<vector<ll>> distances(n, vector<ll>(m, 1e9));
  distances[0][0] = 0;
  pq.push({0, {0, 0}});

  while (!pq.empty()) {
    auto [current_distance, current_point] = pq.top();
    auto [current_y, current_x] = current_point;
    pq.pop();

    for (const auto& [weight_y, weight_x] : weights) {
      auto next_y = current_y + weight_y;
      auto next_x = current_x + weight_x;

      if (next_x < 0 || next_x >= m || next_y < 0 || next_y >= n) continue;
      if (distances[next_y][next_x] >
          current_distance + graph[next_y][next_x]) {
        distances[next_y][next_x] = current_distance + graph[next_y][next_x];
        pq.push({distances[next_y][next_x], {next_y, next_x}});
      }
    }
  }

  return distances[n - 1][m - 1];
}

int main() {
  cin.tie(0);
  std::ios_base::sync_with_stdio(false);

  int n, m;
  cin >> m >> n;
  vector<vector<int>> graph(n, vector<int>(m));

  string temp;
  for (int i = 0; i < n; i++) {
    cin >> temp;
    for (int j = 0; j < m; j++) {
      graph[i][j] = temp.at(j) - '0';
    }
  }

  cout << dijkstra(graph, n, m);
  return 0;
}