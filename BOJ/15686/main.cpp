#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios::sync_with_stdio(false);
using namespace std;

int N, M;
vector<vector<int>> board;
vector<pair<int, int>> houses, chickens;
int ans = 1e9;

void dfs(int start, int cnt, vector<int>& selected) {
  if (cnt == M) {
    int total_distance = 0;
    for (const auto& [hy, hx] : houses) {
      int min_distance = 1e9;
      for (const auto& idx : selected) {
        auto [cy, cx] = chickens[idx];
        min_distance = min(min_distance, abs(hy - cy) + abs(hx - cx));
      }
      total_distance += min_distance;
    }
    ans = min(ans, total_distance);
    return;
  }
  for (int i = start; i < chickens.size(); i++) {
    selected.push_back(i);
    dfs(i + 1, cnt + 1, selected);
    selected.pop_back();
  }
}

int main() {
  FastIO;

  cin >> N >> M;
  board.resize(N, vector<int>(N));
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      cin >> board[i][j];
      if (board[i][j] == 1)
        houses.emplace_back(i, j);
      else if (board[i][j] == 2)
        chickens.emplace_back(i, j);
    }
  }

  vector<int> selected;
  dfs(0, 0, selected);
  cout << ans << "\n";
  return 0;
}