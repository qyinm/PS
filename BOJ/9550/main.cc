#include <bits/stdc++.h>

using namespace std;

int main() {
  int tc;
  cin >> tc;

  while (tc--) {
    int n, k, count, ans = 0;
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
      cin >> count;
      ans += count / k;
    }
    cout << ans << "\n";
  }
}