#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;
using ll = long long;
using pil = pair<int, ll>;

vector<vector<pil>> graph;
vector<bool> visited;
int N;

ll dfs(int curr, ll total) {
  ll curr_total = total;
  for (const auto& [nxt, nw] : graph[curr]) {
    if (visited[nxt]) continue;
    visited[nxt] = true;
    curr_total = max(curr_total, dfs(nxt, total + nw));
  }
  return curr_total;
}

int main() {
  FastIO;
  cin >> N;
  graph = vector<vector<pil>>(N + 1);

  for (int i = 0; i < N - 1; i++) {
    int a, b, w;
    cin >> a >> b >> w;
    graph[a].push_back({b, w});
    graph[b].push_back({a, w});
  }

  ll ans = -1;
  for (int i = 1; i <= N; i++) {
    visited = vector<bool>(N + 1, false);
    visited[i] = true;
    ans = max(ans, dfs(i, 0));
  }

  cout << ans;
}