#include <iostream>
#include <vector>

using namespace std;
using pii = pair<int, int>;
using ll = long long;

vector<ll> bellman_ford(const vector<vector<pii>>& graph, int v) {
  vector<ll> distances(v, 1e9);
  distances[0] = 0;

  for (int k = 0; k < v - 1; k++) {
    for (int u = 0; u < v; u++) {
      if (distances[u] == 1e9) continue;
      for (const auto& [next_vertex, next_cost] : graph[u]) {
        distances[next_vertex] =
            min(distances[next_vertex], distances[u] + next_cost);
      }
    }
  }

  return distances;
}

bool check_cycle(int v, vector<ll>& distances,
                 const vector<vector<pii>>& graph) {
  vector<ll> temp = distances;
  for (int u = 0; u < v; u++) {
    for (const auto& [next_vertex, next_cost] : graph[u]) {
      temp[next_vertex] = min(temp[next_vertex], temp[u] + next_cost);
    }
  }
  for (int i = 0; i < v; i++) {
    if (distances[i] != temp[i] && distances[i] != 1e9) {
      return true;
    }
  }

  return false;
}

int main() {
  int v, e;
  cin >> v >> e;
  vector<vector<pii>> graph(v);

  for (int i = 0; i < e; i++) {
    int from, to, cost;
    cin >> from >> to >> cost;
    graph[from - 1].push_back({to - 1, cost});
  }

  vector<ll> distances = bellman_ford(graph, v);

  if (check_cycle(v, distances, graph)) {
    cout << "-1\n";
    return 0;
  }
  for (int i = 1; i < v; i++) {
    if (distances[i] == 1e9) {
      cout << "-1\n";
      continue;
    }
    cout << distances[i] << "\n";
  }
  return 0;
}