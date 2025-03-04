#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false)

using namespace std;
using pi = pair<int, int>;
using iii = tuple<int, int, int>;
using tpi = tuple<pi, iii>;
vector<pi> directions = {{-1, 0}, {-1, 1}, {0, 1},  {1, 1},
                         {1, 0},  {1, -1}, {0, -1}, {-1, -1}};
int N, M, K;
int main() {
  FastIO;
  cin >> N >> M >> K;
  vector<vector<vector<iii>>> board(N, vector<vector<iii>>(N));  // 무게, 방향
  queue<tpi> q;
  int r, c, m, s, d;
  while (M--) {
    cin >> r >> c >> m >> s >> d;
    q.push({{r, c}, {m, s, d}});
  }
  while (K--) {
    while (!q.empty()) {
      auto [point, info] = q.front();
      auto [y, x] = point;
      auto [m, s, d] = info;
      q.pop();

      int ny = (y + s * directions[d].first) % N;
      int nx = (x + s * directions[d].second) % N;
      if (ny < 0) ny += N;
      if (nx < 0) nx += N;
      //   cout << ny << " " << nx << endl;
      board[ny][nx].emplace_back(m, s, d);
    }
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        if (board[i][j].size() == 0) continue;
        int flag = 0;
        int next_m = 0;
        int next_s = 0;
        for (const auto& [m, s, d] : board[i][j]) {
          //   cout << m << " " << s << " " << d << "\n";
          flag += d % 2;
          next_m += m;
          next_s += s;
        }
        if (board[i][j].size() == 1) {
          q.push({{i, j}, {next_m, next_s, get<2>(board[i][j][0])}});
          board[i][j].clear();
          continue;
        }
        next_m /= 5;
        next_s /= board[i][j].size();
        int start = 1;
        if (flag == board[i][j].size() || flag == 0) {
          start = 0;
        }
        board[i][j].clear();
        if (next_m == 0) continue;

        for (int next_d = start; next_d < 8; next_d += 2) {
          //   cout << "small : " << i << " " << j << ", " << next_m << ", "
          //        << next_s << ", " << next_d << endl;
          q.push({{i, j}, {next_m, next_s, next_d}});
        }
      }
    }
  }
  int ans = 0;
  while (!q.empty()) {
    auto [_, info] = q.front();
    q.pop();
    auto [m, a, b] = info;
    ans += m;
  }
  cout << ans;

  return 0;
}