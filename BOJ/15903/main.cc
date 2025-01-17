#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;
using ll = long long;

int N, M;

int main() {
  FastIO;
  cin >> N >> M;
  priority_queue<ll, vector<ll>, greater<>> pq;

  for (int i = 0; i < N; i++) {
    ll temp;
    cin >> temp;
    pq.push(temp);
  }

  while (M--) {
    ll a = pq.top();
    pq.pop();
    ll b = pq.top();
    pq.pop();

    pq.push(a + b);
    pq.push(a + b);
    // cout << a << " " << b << endl;
  }

  ll ans = 0;
  while (!pq.empty()) {
    ans += pq.top();
    pq.pop();
  }

  cout << ans;

  return 0;
}