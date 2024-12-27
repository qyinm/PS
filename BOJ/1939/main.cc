#include <iostream>
#include <queue>
#include <vector>

using namespace std;
using ll = long long;
using pli = pair<long, int>;

int search(const vector<vector<pli>>& graph, int from, int to) {
  priority_queue<pli> pq;
  vector<ll> distances(graph.size() + 1, -1);
  pq.push({1e9, from});

  while (!pq.empty()) {
    auto [cur_cost, cur_node] = pq.top();
    pq.pop();
    if (cur_node == to) break;

    for (auto [next_cost, next_node] : graph[cur_node]) {
      int cost = min(cur_cost, next_cost);
      if (distances[next_node] < cost) {
        distances[next_node] = cost;
        pq.push({cost, next_node});
      }
    }
  }

  return distances[to];
}

int main() {
  cin.tie(0);
  std::ios_base::sync_with_stdio(false);

  int n, m;
  cin >> n >> m;
  vector<vector<pli>> graph(n + 1);

  while (m--) {
    int a, b, cost;
    cin >> a >> b >> cost;
    graph[a].push_back({cost, b});
    graph[b].push_back({cost, a});
  }
  int from, to;
  cin >> from >> to;

  cout << search(graph, from, to);
}