#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios::sync_with_stdio(false);

using namespace std;

int main() {
  FastIO;

  int N;
  cin >> N;

  vector<vector<int>> graph(N, vector<int>(N, 1e9));
  for (int i = 0; i < N; i++) {
    graph[i][i] = 0;
  }

  while (true) {
    int a, b;
    cin >> a >> b;
    if (a == -1 && b == -1) break;
    graph[a - 1][b - 1] = 1;
    graph[b - 1][a - 1] = 1;
  }

  for (int k = 0; k < N; k++) {
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);
      }
    }
  }

  vector<int> scores(N);
  int minScore = 1e9;
  for (int i = 0; i < N; i++) {
    int mx = 0;
    for (int j = 0; j < N; j++) {
      mx = max(mx, graph[i][j]);
    }
    scores[i] = mx;
    minScore = min(minScore, mx);
  }

  vector<int> candidates;
  for (int i = 0; i < N; i++) {
    if (scores[i] == minScore) candidates.push_back(i + 1);
  }

  cout << minScore << " " << candidates.size() << "\n";
  for (auto c : candidates) {
    cout << c << " ";
  }
  return 0;
}