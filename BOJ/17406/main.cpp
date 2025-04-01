#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;
using tti = tuple<int, int, int>;
using ll = long long;

int N, M, K;

void move_board(int r, int c, int s, vector<vector<int>>& board) {
  while (s > 0) {
    int start_y = r - s;
    int start_x = c - s;

    int end_y = r + s;
    int end_x = c + s;

    int temp = board[start_y][start_x];
    for (int ty = start_y; ty < end_y; ty++) {
      board[ty][start_x] = board[ty + 1][start_x];
    }
    for (int tx = start_x; tx < end_x; tx++) {
      board[end_y][tx] = board[end_y][tx + 1];
    }
    for (int ty = end_y; ty > start_y; ty--) {
      board[ty][end_x] = board[ty - 1][end_x];
    }
    for (int tx = end_x; tx > start_x + 1; tx--) {
      board[start_y][tx] = board[start_y][tx - 1];
    }
    board[start_y][start_x + 1] = temp;
    s--;
  }
}

ll min_val(vector<vector<int>> board) {
  ll ret = 1e9;
  for (const auto& row : board) {
    ret = min(ret, accumulate(row.begin(), row.end(), 0LL));
  }

  return ret;
}

int main() {
  FastIO;
  cin >> N >> M >> K;
  vector<vector<int>> board = vector<vector<int>>(N, vector<int>(M));

  for (auto& row : board) {
    for (auto& el : row) {
      cin >> el;
    }
  }

  vector<tti> v;
  while (K--) {
    int r, c, s;
    cin >> r >> c >> s;
    v.push_back({r - 1, c - 1, s});
  }
  sort(v.begin(), v.end());

  ll ans = 1e9;
  do {
    auto temp = board;
    for (const auto& [r, c, s] : v) {
      //   cout << r << c << s << "/";
      //   cout << endl;
      move_board(r, c, s, temp);

      //   for (const auto& r : temp) {
      //     for (const auto& e : r) {
      //       cout << e << " ";
      //     }
      //     cout << endl;
      //   }
      //   cout << endl;
    }
    ans = min(ans, min_val(temp));
  } while (next_permutation(v.begin(), v.end()));

  cout << ans;

  return 0;
}