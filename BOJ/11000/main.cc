#include <iostream>
#include <queue>

using namespace std;
using pii = pair<int, int>;

int main() {
  cin.tie(0);
  std::ios_base::sync_with_stdio(false);

  int n;
  cin >> n;

  vector<pii> v;
  priority_queue<int, vector<int>, greater<>> pq;

  while (n--) {
    int s, t;
    cin >> s >> t;

    v.push_back({s, t});
  }

  sort(v.begin(), v.end());
  pq.push(v[0].second);

  for (int i = 1; i < v.size(); i++) {
    if (pq.top() <= v[i].first) {
      pq.pop();
    }
    pq.push(v[i].second);
  }

  cout << pq.size();
}