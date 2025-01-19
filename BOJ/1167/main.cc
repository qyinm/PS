#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;
using ll = long long;
using pil = pair<int, ll>;

vector<vector<pil>> graph;
vector<bool> visited;
int N;

pil dfs(int curr, ll dist) {
  visited[curr] = true;
  pil ret = {curr, dist};

  for (const auto& [nxt, nw] : graph[curr]) {
    if (!visited[nxt]) {
      auto [farthest_node, max_dist] = dfs(nxt, dist + nw);
      if (max_dist > ret.second) {
        ret = {farthest_node, max_dist};
      }
    }
  }
  return ret;
}

int main() {
  FastIO;
  cin >> N;
  graph = vector<vector<pil>>(N + 1);

  for (int i = 0; i < N; i++) {
    int a, b, w;
    cin >> a;
    while (true) {
      cin >> b;
      if (b == -1) break;
      cin >> w;
      graph[a].push_back({b, w});
      graph[b].push_back({a, w});
    }
  }

  visited = vector<bool>(N + 1, false);
  auto [farthest_node, _] = dfs(1, 0);
  {
    visited = vector<bool>(N + 1, false);
    auto [_, longest_dist] = dfs(farthest_node, 0);

    cout << longest_dist;
  }
}