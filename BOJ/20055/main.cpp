#include <iostream>
#include <vector>
using namespace std;
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false)

int n, k;
vector<pair<int, bool>> belt;
int start = 0;

bool isOver() {
  int cnt = 0;
  for (int i = 0; i < 2 * n; i++) {
    if (belt[i].first == 0) cnt++;
  }
  return cnt >= k;
}

int main() {
  FastIO;
  cin >> n >> k;
  belt.resize(2 * n);
  for (int i = 0; i < 2 * n; i++) {
    cin >> belt[i].first;
    belt[i].second = false;
  }

  int step = 0;
  while (true) {
    step++;
    // 1. 벨트 회전
    start = (start - 1 + 2 * n) % (2 * n);
    int unload = (start + n - 1) % (2 * n);
    if (belt[unload].second) {
      belt[unload].second = false;
    }

    // 2. 로봇 이동
    for (int i = n - 2; i >= 0; i--) {
      int pos = (start + i) % (2 * n);
      if (!belt[pos].second) continue;
      int next = (pos + 1) % (2 * n);
      if (!belt[next].second && belt[next].first > 0) {
        belt[pos].second = false;
        if (next == unload) {
          // 내리는 위치에 도착하면 로봇 제거
        } else {
          belt[next].second = true;
        }
        belt[next].first--;
      }
    }

    // 3. 로봇 올리기
    if (belt[start].first > 0 && !belt[start].second) {
      belt[start].second = true;
      belt[start].first--;
    }

    // 4. 종료 조건 검사
    if (isOver()) break;
  }

  cout << step << "\n";
  return 0;
}