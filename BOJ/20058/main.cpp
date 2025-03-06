#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;
using pi = pair<int, int>;
int N, Q, L, gridSize;
vector<vector<int>> board, new_board;
vector<pi> weights = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

int bfs(int y, int x, vector<vector<bool>>& visited) {
  queue<pi> q;
  q.push({y, x});
  int cnt = 1;
  visited[y][x] = true;

  while (!q.empty()) {
    auto [cy, cx] = q.front();
    q.pop();

    for (const auto& [wy, wx] : weights) {
      int ny = cy + wy;
      int nx = cx + wx;
      if (ny < 0 || ny >= gridSize || nx < 0 || nx >= gridSize) continue;
      if (visited[ny][nx] || board[ny][nx] <= 0) continue;
      visited[ny][nx] = true;
      q.push({ny, nx});
      ++cnt;
    }
  }
  return cnt;
}

void rotate() {
  int sub = (1 << L);
  new_board = board;
  for (int y = 0; y < gridSize; y += sub) {
    for (int x = 0; x < gridSize; x += sub) {
      for (int i = 0; i < sub; i++) {
        for (int j = 0; j < sub; j++) {
          new_board[y + j][x + sub - 1 - i] = board[y + i][x + j];
        }
      }
    }
  }
  board = new_board;
}

void meltIce() {
  queue<pi> q;
  for (int y = 0; y < gridSize; y++) {
    for (int x = 0; x < gridSize; x++) {
      int cnt = 0;
      for (const auto& [wy, wx] : weights) {
        int ny = y + wy;
        int nx = x + wx;
        if (ny < 0 || ny >= gridSize || nx < 0 || nx >= gridSize) {
          continue;
        };
        if (board[ny][nx] > 0) cnt++;
      }
      if (cnt < 3) {
        q.push({y, x});
      }
    }
  }
  while (!q.empty()) {
    auto [y, x] = q.front();
    board[y][x] = max(board[y][x] - 1, 0);
    q.pop();
  }
}

int main() {
  FastIO;
  cin >> N >> Q;
  gridSize = (1 << N);
  board.resize(gridSize, vector<int>(gridSize, 0));
  for (auto& row : board) {
    for (auto& b : row) {
      cin >> b;
    }
  }

  while (Q--) {
    cin >> L;
    rotate();
    meltIce();
  }
  int sum = 0;
  int maxx = 0;
  vector<vector<bool>> visited(gridSize, vector<bool>(gridSize));
  for (int i = 0; i < gridSize; i++) {
    for (int j = 0; j < gridSize; j++) {
      sum += board[i][j];
      if (visited[i][j] || board[i][j] <= 0) continue;
      maxx = max(maxx, bfs(i, j, visited));
    }
  }
  cout << sum << "\n" << maxx;

  return 0;
}