#include <bits/stdc++.h>
#define FastIO cin.tie(NULL)->ios_base::sync_with_stdio(false);

using namespace std;
using ll = long long;
using pll = pair<ll, ll>;

class Edge {
 public:
  int weight;
  int next;
  Edge(int w, int n) : weight(w), next(n) {};
};

int n, r, m;
vector<vector<Edge>> graph;
vector<int> items;

ll dijkstra(int start) {
  vector<ll> distances(n, 1e9);
  priority_queue<pll, vector<pll>, greater<>> pq;
  pq.push({0, start});
  distances[start] = 0;

  ll ret = 0;
  while (!pq.empty()) {
    auto [cw, cn] = pq.top();
    pq.pop();

    for (const auto& node : graph[cn]) {
      if (distances[node.next] > cw + node.weight) {
        distances[node.next] = cw + node.weight;
        pq.push({cw + node.weight, node.next});
      }
    }
  }
  for (int i = 0; i < n; i++) {
    if (distances[i] <= m) {
      ret += items[i];
    }
  }
  return ret;
}

int main() {
  FastIO;
  cin >> n >> m >> r;
  graph = vector<vector<Edge>>(n);
  items = vector<int>(n);
  for (auto& item : items) {
    cin >> item;
  }
  for (int i = 0; i < r; i++) {
    int a, b, c;
    cin >> a >> b >> c;
    graph[a - 1].push_back(Edge(c, b - 1));
    graph[b - 1].push_back(Edge(c, a - 1));
  }

  ll mm = 0;
  for (int i = 0; i < n; i++) {
    mm = max(mm, dijkstra(i));
  }

  cout << mm;
  return 0;
}