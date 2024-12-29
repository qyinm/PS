#include <iostream>
#include <queue>

using namespace std;
using ll = long long;

ll solve() {
  int n;
  cin >> n;

  ll answer = 0;
  vector<ll> arr(n);
  for (auto& a : arr) {
    cin >> a;
  }

  ll maxx = arr[n - 1];
  for (int idx = n - 2; idx >= 0; idx--) {
    if (arr[idx] <= maxx) {
      answer += maxx - arr[idx];
    } else {
      maxx = arr[idx];
    }
  }

  return answer;
}

int main() {
  cin.tie(0);
  std::ios_base::sync_with_stdio(false);
  int tc;
  cin >> tc;

  while (tc--) {
    cout << solve() << "\n";
  }
}