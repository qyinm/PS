#include <bits/stdc++.h>
#define FastIO cin.tie(NULL)->ios_base::sync_with_stdio(false);

using namespace std;
using pii = pair<int, int>;

int main() {
  FastIO;

  int n;
  cin >> n;
  vector<pii> v(n);
  vector<int> answer(n);

  for (int i = 0; i < n; i++) {
    int a;
    cin >> a;
    v[i] = {a, i};
  }

  sort(v.begin(), v.end());

  int order = 0;
  for (const auto& [value, index] : v) {
    answer[index] = order++;
  }

  for (const auto& ans : answer) {
    cout << ans << " ";
  }
}