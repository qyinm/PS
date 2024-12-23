#include <iostream>
#include <queue>
#include <vector>

using namespace std;
using pii = pair<int, int>;
using ll = long long;

vector<pii> weights = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

ll dijkstra(const vector<vector<int>>& graph, const int& n) {
  priority_queue<pair<ll, pii>, vector<pair<ll, pii>>, greater<>> pq;
  vector<vector<ll>> distances(n, vector<ll>(n, 1e9));
  pq.push({graph[0][0], {0, 0}});
  distances[0][0] = graph[0][0];

  while (!pq.empty()) {
    auto [cost, current] = pq.top();
    pq.pop();

    for (const auto& [weight_y, weight_x] : weights) {
      int next_y = current.first + weight_y;
      int next_x = current.second + weight_x;

      if (next_x < 0 || next_x >= n || next_y < 0 || next_y >= n) continue;
      int next_cost = cost + graph[next_y][next_x];
      if (distances[next_y][next_x] > next_cost) {
        distances[next_y][next_x] = next_cost;
        pq.push({next_cost, {next_y, next_x}});
      }
    }
  }

  return distances[n - 1][n - 1];
}

int main() {
  int n, index = 1;
  vector<vector<int>> graph;
  while (cin >> n && n != 0) {
    graph = vector<vector<int>>(n, vector<int>(n));
    for (auto& row : graph) {
      for (auto& item : row) {
        cin >> item;
      }
    }

    cout << "Problem " << index++ << ": " << dijkstra(graph, n) << "\n";
  }
}