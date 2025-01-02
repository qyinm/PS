#include <bits/stdc++.h>
#define FastIO cin.tie(NULL)->ios_base::sync_with_stdio(false);

using namespace std;

int n;
vector<vector<int>> graph;
vector<int> in;
vector<int> out;

void bfs(int start, vector<int>& in, vector<int>& out) {
  vector<bool> visited(n + 1);
  queue<int> q;
  visited[start] = true;
  q.push(start);

  int count_node = 0;
  while (!q.empty()) {
    int current = q.front();
    q.pop();

    for (const auto& next : graph[current]) {
      if (visited[next]) continue;
      q.push(next);
      visited[next] = true;
      in[next] += 1;
      count_node++;
    }
  }
  out[start] = count_node;
}

int main() {
  int m;
  cin >> n >> m;
  graph = vector<vector<int>>(n + 1);

  for (int i = 0; i < m; i++) {
    int a, b;
    cin >> a >> b;
    graph[b].push_back(a);
  }

  int answer = 0;
  in = vector<int>(n + 1);
  out = vector<int>(n + 1);
  for (int i = 1; i <= n; i++) {
    bfs(i, in, out);
  }

  int edge_value = (n - 1) / 2;
  for (int i = 1; i <= n; i++) {
    if (in[i] > edge_value || out[i] > edge_value) {
      answer++;
    }
  }

  cout << answer;
}