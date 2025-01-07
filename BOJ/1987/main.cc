#include <bits/stdc++.h>
#define FastIO cin.tie(NULL)->ios_base::sync_with_stdio(false);

using namespace std;

int R, C;
char graph[20][20];
int max_tile = 1;
pair<int, int> weights[] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
bool visited[26] = {false};

void dfs(int cur_r, int cur_c, int count) {
  bool flag = true;

  for (const auto& [wr, wc] : weights) {
    int nr = cur_r + wr;
    int nc = cur_c + wc;

    if (nr < 0 || nr >= R || nc < 0 || nc >= C) continue;
    if (visited[graph[nr][nc] - 'A']) continue;
    visited[graph[nr][nc] - 'A'] = true;
    dfs(nr, nc, count + 1);
    visited[graph[nr][nc] - 'A'] = false;
    flag = false;
  }

  if (flag) {
    max_tile = max(max_tile, count);
  }

  return;
}

int main() {
  FastIO;
  cin >> R >> C;
  for (int r = 0; r < R; r++) {
    for (int c = 0; c < C; c++) {
      cin >> graph[r][c];
    }
  }

  visited[graph[0][0] - 'A'] = true;
  dfs(0, 0, 1);
  cout << max_tile;
}