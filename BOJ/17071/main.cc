#include <bits/stdc++.h>
#define FastIO cin.tie(NULL)->ios_base::sync_with_stdio(false);

using namespace std;

int N, K;

const int MAX_POSITION = 500000;

int bfs() {
  bool visited[2][MAX_POSITION + 1];
  memset(visited, false, sizeof(visited));

  queue<int> q;
  q.push(N);
  int time = 0;
  visited[0][N] = 0;

  while (!q.empty()) {
    if (K > MAX_POSITION) return -1;
    if (visited[time % 2][K]) {
      return time;
    }

    int size = q.size();
    for (int k = 0; k < size; k++) {
      int cur = q.front();
      q.pop();

      if (cur == K) {
        return time;
      }
      int moves[] = {cur + 1, cur - 1, cur * 2};
      for (const auto& move : moves) {
        // cout << time << " " << cur << " " << move << " " << K << endl;
        if (move < 0 || move > MAX_POSITION) continue;
        if (visited[(time + 1) % 2][move]) continue;
        q.push(move);
        visited[(time + 1) % 2][move] = true;
      }
    }
    time++;
    K += time;
  }

  return -1;
}

int main() {
  FastIO;
  cin >> N >> K;

  cout << bfs() << endl;

  return 0;
}

/**

8725 328744
-1

27297 339652
425

34768 292340
-1

438 129118
95

4040 160532
385

300000 0
-1

7 37 5

10 57 5

21 70 4

18 58 4

18 66 4

16 50 4

34 0 8
*/