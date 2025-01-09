#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;

int N;
int graph[100][100];
pair<int, int> weights[] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

void grouping(queue<pair<int, int>> island_q) {
  int start_idx = -1;
  while (!island_q.empty()) {
    auto [curr_y, curr_x] = island_q.front();
    island_q.pop();

    if (graph[curr_y][curr_x] < 0) continue;
    graph[curr_y][curr_x] = start_idx;

    queue<pair<int, int>> tempq;
    tempq.push({curr_y, curr_x});
    while (!tempq.empty()) {
      auto [c_y, c_x] = tempq.front();
      tempq.pop();
      for (const auto& [w_y, w_x] : weights) {
        int ny = c_y + w_y;
        int nx = c_x + w_x;

        if (ny < 0 || ny >= N || nx < 0 || nx >= N) continue;
        if (graph[ny][nx] <= 0) continue;
        graph[ny][nx] = start_idx;
        tempq.push({ny, nx});
      }
    }
    start_idx--;
  }
}

void find_shortest_bridge(queue<pair<int, int>> islandq) {
  bool check_group[51];
  memset(check_group, false, sizeof(check_group));
  int min_length = 200;

  while (!islandq.empty()) {
    auto [start_y, start_x] = islandq.front();
    int start_point = graph[start_y][start_x];
    islandq.pop();

    // if (check_group[-start_point]) continue;
    // check_group[-start_point] = true;

    bool visited[100][100];
    memset(visited, false, sizeof(visited));

    queue<tuple<int, int, int>> q;
    q.push({0, start_y, start_x});
    visited[start_y][start_x] = true;
    // cout << start_y << " " << start_x << endl;

    while (!q.empty()) {
      auto [cost, curr_y, curr_x] = q.front();
      q.pop();

      for (const auto& [w_y, w_x] : weights) {
        int ny = curr_y + w_y;
        int nx = curr_x + w_x;
        int next_point = graph[ny][nx];

        if (ny < 0 || ny >= N || nx < 0 || nx >= N) continue;
        if (visited[ny][nx]) continue;
        visited[ny][nx] = true;

        if (next_point == 0) {
          q.push({cost + 1, ny, nx});
        } else if (next_point == start_point) {
          q.push({0, ny, nx});
        } else if (next_point != start_point) {
          min_length = min(min_length, cost);
          q.push({cost, ny, nx});
        }
      }
    }
  }
  cout << min_length;
}

int main() {
  FastIO;
  cin >> N;

  queue<pair<int, int>> island_q;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      cin >> graph[i][j];
      if (graph[i][j] == 1) {
        island_q.push({i, j});
      }
    }
  }
  grouping(island_q);
  find_shortest_bridge(island_q);

  return 0;
}