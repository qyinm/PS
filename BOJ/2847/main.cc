#include <bits/stdc++.h>
#define FastIO cin.tie(NULL)->ios_base::sync_with_stdio(false);

using namespace std;

int main() {
  int n;
  cin >> n;

  vector<int> v(n);
  for (auto& vv : v) {
    cin >> vv;
  }

  int answer = 0;
  for (int i = n - 2; i >= 0; i--) {
    if (v[i] >= v[i + 1]) {
      answer += v[i] - (v[i + 1] - 1);
      v[i] = v[i + 1] - 1;
    }
  }

  cout << answer;
}