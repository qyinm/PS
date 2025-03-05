#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;

vector<vector<tuple<int, int, double>>> directions = {{{-2, 0, 0.02},
                                                       {-1, 0, 0.07},
                                                       {-1, 1, 0.01},
                                                       {2, 0, 0.02},
                                                       {1, 0, 0.07},
                                                       {1, 1, 0.01},
                                                       {-1, -1, 0.1},
                                                       {1, -1, 0.1},
                                                       {0, -2, 0.05}},
                                                      // 위쪽 방향 기준

                                                      {{-2, 0, 0.05},
                                                       {1, 1, 0.01},
                                                       {-1, -1, 0.1},
                                                       {0, 2, 0.02},
                                                       {0, -1, 0.07},
                                                       {0, 1, 0.07},
                                                       {-1, 1, 0.1},
                                                       {0, -2, 0.02},
                                                       {1, -1, 0.01}},

                                                      // 오른쪽 방향 기준
                                                      {{-2, 0, 0.02},
                                                       {-1, 0, 0.07},
                                                       {-1, -1, 0.01},
                                                       {2, 0, 0.02},
                                                       {1, 0, 0.07},
                                                       {1, -1, 0.01},
                                                       {-1, 1, 0.1},
                                                       {1, 1, 0.1},
                                                       {0, 2, 0.05}},

                                                      // 아래쪽 방향 기준
                                                      {{2, 0, 0.05},
                                                       {-1, 1, 0.01},
                                                       {1, -1, 0.1},
                                                       {0, 2, 0.02},
                                                       {0, -1, 0.07},
                                                       {0, 1, 0.07},
                                                       {1, 1, 0.1},
                                                       {0, -2, 0.02},
                                                       {-1, -1, 0.01}}};
vector<vector<int>> board;
int N, out_sand;

void init_board() {
  for (auto& row : board) {
    for (auto& b : row) {
      cin >> b;
    }
  }
}

void move(int next_y, int next_x, int curr_y, int curr_x, int d) {
  int scattered = 0;
  int base = board[curr_y][curr_x];
  for (const auto& [wy, wx, weight] : directions[d]) {
    int sand_y = curr_y + wy;
    int sand_x = curr_x + wx;

    if (sand_y < 0 || sand_y >= N || sand_x < 0 || sand_x >= N) {
      out_sand += base * weight;
    }
    //   if (curr_y == 1 && curr_x == 0) cout << base * weight << endl;
    else {
      board[sand_y][sand_x] += base * weight;
    }
    scattered += base * weight;
  }
  int alpha = base - scattered;
  if (next_y < 0 || next_y >= N || next_x < 0 || next_x >= N) {
    out_sand += alpha;
  } else {
    board[next_y][next_x] += alpha;
  }
  board[curr_y][curr_x] = 0;
}

int main() {
  FastIO;
  cin >> N;
  board.resize(N, vector<int>(N));
  init_board();

  int x = N / 2;
  int y = N / 2;
  int dist = 1;
  int sw = -1;
  for (int i = 0; i < N - 1; i++) {
    // x축 이동
    for (int j = 0; j < dist; j++) {
      x += sw;
      if (board[y][x] == 0) {
        continue;
      }
      move(y, x + sw, y, x, 1 + sw);
    }
    sw *= -1;
    // y축 이동
    for (int j = 0; j < dist; j++) {
      y += sw;
      if (board[y][x] == 0) {
        continue;
      }
      move(y + sw, x, y, x, 2 + sw);
    }

    dist += 1;
  }
  for (int j = 0; j < dist - 1; j++) {
    x += sw;
    if (board[y][x] == 0) {
      continue;
    }
    move(y, x + sw, y, x, 0);
  }
  cout << out_sand;
  return 0;
}