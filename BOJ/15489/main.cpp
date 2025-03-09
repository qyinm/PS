#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false)

using namespace std;

int main() {
  FastIO;
  vector<vector<int>> tries = {{1}};
  int R, C, W;
  cin >> R >> C >> W;
  for (int i = 0; i < R + W; i++) {
    vector<int> vec = {1};
    for (int j = 0; j < i; j++) {
      vec.push_back(tries[i][j] + tries[i][j + 1]);
    }
    vec.push_back(1);
    tries.push_back(vec);
  }

  int ans = 0;
  for (int i = 0; i < W; i++) {
    for (int j = 0; j <= i; j++) {
      ans += tries[R - 1 + i][C - 1 + j];
    }
  }
  cout << ans;
  return 0;
}