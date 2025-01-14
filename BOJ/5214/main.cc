#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;
using pii = pair<int, int>;

int N, K, M;
vector<vector<int>> tube;
vector<vector<int>> station;

int bfs() {
  vector<int> distances(N + 1, 1e9);
  vector<bool> visited(M, false);
  priority_queue<pii, vector<pii>, greater<>> q;
  distances[1] = 1;
  for (const auto& s : station[1]) {
    q.push({1, s});
  }

  while (!q.empty()) {
    auto [cost, t] = q.top();
    q.pop();
    visited[t] = true;

    for (const auto& s : tube[t]) {
      if (distances[s] > cost + 1) {
        distances[s] = cost + 1;
        for (const auto& nt : station[s]) {
          if (visited[nt]) continue;
          // visited[nt] = true;
          q.push({cost + 1, nt});
        }
      }
      if (s == N) return min(distances[s], cost + 1);
    }
  }

  return -1;
}

int main() {
  FastIO;
  cin >> N >> K >> M;

  tube = vector<vector<int>>(M);
  station = vector<vector<int>>(N + 1);
  for (int i = 0; i < M; i++) {
    for (int j = 0; j < K; j++) {
      int t;
      cin >> t;
      tube[i].push_back(t);
      station[t].push_back(i);
    }
  }

  cout << bfs();

  return 0;
}