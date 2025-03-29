#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;

char board[1025][2048];
int N;
int max_row;
int max_height;

void recursion(int n, int x, int y) {
  //   print();
  int row_len = pow(2, n + 1) - 3;
  int height = pow(2, n) - 1;
  int weight = n % 2 == 1 ? -1 : 1;
  int next_step = (height + 1) / 2;
  if (n == 1) {
    board[y][x] = '*';
    // printf("n: %d, x: %d, y: %d, nx: %d, ny: %d, row_len: %d\n", n, x, y,
    //        x + next_step, y + weight * (next_step - 1), row_len);
    return;
  }
  for (int wx = 0; wx < row_len; wx++) {
    board[y][x + wx] = '*';
  }
  for (int wy = 0; wy < height; wy++) {
    board[y + weight * wy][x + wy] = '*';
    board[y + weight * wy][x + row_len - 1 - wy] = '*';
  }
  //   printf("n: %d, x: %d, y: %d, nx: %d, ny: %d, row_len: %d\n", n, x, y,
  //          x + next_step, y + weight * (next_step - 1), row_len);
  recursion(n - 1, x + next_step, y + weight * (next_step - 1));
}

int main() {
  FastIO;
  cin >> N;
  max_row = pow(2, N + 1) - 3;
  max_height = pow(2, N) - 1;
  if (N % 2 == 0) {
    recursion(N, 0, 0);
  } else {
    recursion(N, 0, max_height - 1);
  }

  int weight = -1;
  if (N % 2 == 1) {
    // cout << max_row << endl;
    max_row = (max_row / 2) + 1;
    weight = 1;
  }
  for (int y = 0; y < max_height; y++) {
    for (int x = 0; x < max_row; x++) {
      if (board[y][x] != '*') {
        cout << " ";
        continue;
      }
      cout << board[y][x];
    }
    cout << "\n";
    max_row += weight;
  }

  return 0;
}