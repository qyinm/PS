#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;
int N, M;

void bfs(const vector<vector<int>>& graph) {
  vector<int> record;
  vector<int> distances(N, -1);
  queue<int> q;
  q.push(0);
  distances[0] = 0;
  record.push_back(0);

  while (!q.empty()) {
    int curr = q.front();
    q.pop();

    for (const auto& nxt : graph[curr]) {
      if (distances[nxt] != -1) continue;
      distances[nxt] = distances[curr] + 1;
      q.push(nxt);
      if (distances[record[0]] > distances[nxt]) continue;
      if (distances[record[0]] < distances[nxt]) {
        record.clear();
      }
      record.push_back(nxt);
    }
  }

  sort(record.begin(), record.end());
  cout << record[0] + 1 << " " << distances[record[0]] << " " << record.size();
}

int main() {
  FastIO;
  cin >> N >> M;

  vector<vector<int>> graph(N);

  for (int i = 0; i < M; i++) {
    int a, b;
    cin >> a >> b;
    a--;
    b--;

    graph[a].push_back(b);
    graph[b].push_back(a);
  }

  bfs(graph);
}