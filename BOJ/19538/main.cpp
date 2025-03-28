#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;
using pi = pair<int, int>;

void print_links(vector<vector<int>> links) {
  for (const auto& node : links) {
    for (const auto& next : node) {
      cout << next << " ";
    }
    cout << endl;
  }
}

int main() {
  FastIO;
  int N, M;
  cin >> N;

  vector<vector<int>> links(N);
  for (auto& node : links) {
    int next_node;
    while ((cin >> next_node) && next_node != 0) {
      node.push_back(next_node - 1);
    }
  }

  vector<int> rumors_time(N, -1);
  vector<bool> visited(N, false);
  queue<pi> q;

  cin >> M;
  for (int i = 0; i < M; i++) {
    int cheater;
    cin >> cheater;
    q.push({cheater - 1, 0});
    visited[cheater - 1] = true;
  }
  while (!q.empty()) {
    auto [current_node, current_time] = q.front();
    rumors_time[current_node] = current_time;
    q.pop();

    for (const auto& next_node : links[current_node]) {
      if (rumors_time[next_node] != -1 || visited[next_node]) {
        continue;
      }
      int cnt = 0;
      for (const auto& relation : links[next_node]) {
        if (rumors_time[relation] != -1) {
          cnt += 1;
        }
      }
      if (cnt * 2 >= links[next_node].size()) {
        q.push({next_node, current_time + 1});
        visited[next_node] = true;
      }
    }
  }

  // print answer
  for (const auto& time : rumors_time) {
    cout << time << " ";
  }
}