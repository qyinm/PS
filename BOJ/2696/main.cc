#include <iostream>
#include <queue>

using namespace std;

void solve() {
  int len;
  cin >> len;

  vector<int> answer;
  priority_queue<int> max_pq;
  priority_queue<int, vector<int>, greater<>> min_pq;

  int data;
  for (int i = 1; i <= len; i++) {
    cin >> data;
    if (i % 2 == 1) {
      max_pq.push(data);
    } else {
      min_pq.push(data);
    }

    if (!min_pq.empty() && !max_pq.empty() && min_pq.top() < max_pq.top()) {
      auto max_top = max_pq.top();
      auto min_top = min_pq.top();
      max_pq.pop();
      min_pq.pop();
      max_pq.push(min_top);
      min_pq.push(max_top);
    }

    if (i % 2 == 1) {
      answer.push_back(max_pq.top());
    }
  }

  int count = (len + 1) / 2;
  cout << count << "\n";
  for (int i = 0; i < count; i++) {
    cout << answer[i] << " ";
    if (i + 1 > 0 && (i + 1) % 10 == 0) {
      cout << "\n";
    }
  }
}

int main() {
  cin.tie(0);
  std::ios_base::sync_with_stdio(false);

  int tc;
  cin >> tc;
  while (tc--) {
    solve();
  }
}