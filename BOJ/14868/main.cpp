#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false)

using namespace std;
using pi = pair<int, int>;

int N, K;
vector<int> parents;

vector<pi> weight = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

int find(int i) {
  if (parents[i] == i) return i;
  return parents[i] = find(parents[i]);
}

void join(int i, int j) {
  int pi = find(i);
  int pj = find(j);

  if (pi != pj) {
    parents[pj] = pi;
  }
}

bool isUnited() {
  int root = find(1);
  for (int i = 2; i <= K; i++) {
    if (find(i) != root) return false;
  }
  return true;
}

int main() {
  FastIO;
  cin >> N >> K;

  vector<vector<int>> board(N, vector<int>(N, 0));
  parents.resize(K + 1);
  for (int i = 1; i <= K; i++) parents[i] = i;

  queue<pi> q;
  int x, y;
  for (int k = 1; k <= K; k++) {
    int x, y;
    cin >> x >> y;
    x -= 1;
    y -= 1;
    board[y][x] = k;  // 문명 번호는 1부터 K까지
    q.push({y, x});
  }
  queue<pi> exq = q;
  while (!q.empty()) {
    auto [cy, cx] = q.front();
    q.pop();

    for (auto [wy, wx] : weight) {
      int ny = cy + wy;
      int nx = cx + wx;

      if (ny < 0 || ny >= N || nx < 0 || nx >= N) continue;
      if (board[ny][nx] != 0) {
        join(board[cy][cx], board[ny][nx]);
      }
    }
  }
  if (isUnited()) {
    cout << 0;
    return 0;
  }

  int time = 0;
  while (!isUnited()) {
    // for (auto p : parents) {
    //   cout << p << " ";
    // }
    // cout << endl;

    int len_q = exq.size();
    while (len_q--) {
      auto [y, x] = exq.front();
      exq.pop();

      for (const auto& [wy, wx] : weight) {
        int ny = y + wy;
        int nx = x + wx;

        if (ny < 0 || ny >= N || nx < 0 || nx >= N) continue;
        if (board[ny][nx] != 0) {
          join(board[ny][nx], board[y][x]);
        } else {
          board[ny][nx] = board[y][x];
          exq.push({ny, nx});

          // 새로 확산된 지점 주변의 문명들과 병합 확인
          for (const auto& nw : weight) {
            int nny = ny + nw.first;
            int nnx = nx + nw.second;

            if (nny < 0 || nny >= N || nnx < 0 || nnx >= N) continue;
            if (board[nny][nnx] != 0) {
              join(board[ny][nx], board[nny][nnx]);
            }
          }
        }
      }
    }
    // for (const auto& row : board) {
    //   for (const auto& el : row) {
    //     cout << el << " ";
    //   }
    //   cout << endl;
    // }
    // cout << endl;
    time++;
  }

  cout << time;

  return 0;
}