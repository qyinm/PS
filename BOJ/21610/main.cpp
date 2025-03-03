#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;
vector<pair<int, int>> directions = {{0, -1}, {-1, -1}, {-1, 0},
                                     {-1, 1}, {0, 1},   {1, 1},
                                     {1, 0},  {1, -1}};  // first: y, second: x
int N, M;
vector<vector<int>> board;

void printBoard() {
  for (const auto& row : board) {
    for (const auto& e : row) {
      cout << e << " ";
    }
    cout << endl;
  }
}

int main() {
  FastIO;
  cin >> N >> M;
  board = vector<vector<int>>(N, vector<int>(N));
  for (auto& row : board) {
    for (auto& e : row) {
      cin >> e;
    }
  }

  queue<pair<int, int>> cloud_pos;
  // 초기 구름 위치 추가.
  cloud_pos.push({N - 1, 0});
  cloud_pos.push({N - 1, 1});
  cloud_pos.push({N - 2, 0});
  cloud_pos.push({N - 2, 1});

  while (M--) {
    int direction, weight;
    cin >> direction >> weight;

    int pos_size = cloud_pos.size();
    while (pos_size--) {
      auto [y, x] = cloud_pos.front();
      cloud_pos.pop();
      int ny = (y + directions[direction - 1].first * weight) % N;
      int nx = (x + directions[direction - 1].second * weight) % N;

      if (ny < 0) ny += N;
      if (nx < 0) nx += N;
      // printf("ny : %d, nx: %d\n", ny, nx);
      cloud_pos.push({ny, nx});
      board[ny][nx] += 1;
    }

    queue<tuple<int, int, int>> add_water_q;
    while (!cloud_pos.empty()) {
      auto [y, x] = cloud_pos.front();
      cloud_pos.pop();
      int cnt = 0;
      for (int i = 0; i < 4; i++) {
        auto [wy, wx] = directions[2 * i + 1];
        int ny = y + wy;
        int nx = x + wx;
        if (ny < 0 || ny >= N || nx < 0 || nx >= N) continue;
        if (board[ny][nx] <= 0) continue;
        cnt += 1;
      }
      add_water_q.push({y, x, cnt});
    }

    vector<vector<bool>> prev_clouds(N, vector<bool>(N, false));
    while (!add_water_q.empty()) {
      auto [y, x, plus] = add_water_q.front();
      add_water_q.pop();

      board[y][x] += plus;
      prev_clouds[y][x] = true;
    }

    for (int y = 0; y < N; y++) {
      for (int x = 0; x < N; x++) {
        if (prev_clouds[y][x] || board[y][x] < 2) continue;
        cloud_pos.push({y, x});
        board[y][x] -= 2;
      }
    }
  }

  long long ans = 0;
  for (const auto& row : board) {
    for (const auto& e : row) {
      ans += e;
    }
  }
  cout << ans;

  return 0;
}