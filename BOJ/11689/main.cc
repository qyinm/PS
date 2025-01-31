#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;
using ll = long long;

int main() {
  FastIO;
  ll n;
  cin >> n;

  ll ans = n;
  for (ll i = 2; i * i <= n; i++) {
    if (n % i != 0) continue;
    ans /= i;
    ans *= i - 1;
    while (n % i == 0) {
      n /= i;
    }
  }
  if (n > 1) {
    ans /= n;
    ans *= n - 1;
  }
  cout << ans;

  return 0;
}