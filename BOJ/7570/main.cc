#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;

  vector<int> arr(N), pos(N + 1);
  for (auto& a : arr) {
    cin >> a;
  }
  for (int i = 0; i < N; i++) {
    pos[arr[i]] = i;
  }

  int best = 1, cur = 1;
  for (int x = 1; x < N; x++) {
    if (pos[x + 1] > pos[x]) {
      cur++;
      best = max(best, cur);
    } else {
      cur = 1;
    }
  }

  cout << N - best;
  return 0;
}