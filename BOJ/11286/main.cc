#include <iostream>
#include <queue>

using namespace std;

struct cmp {
  bool operator()(int a, int b) {
    if (abs(a) != abs(b)) {
      return abs(a) > abs(b);
    } else {
      return a > b;
    }
  }
};

priority_queue<int, vector<int>, cmp> pq;

int main() {
  cin.tie(0)->sync_with_stdio(false);
  int tc;
  cin >> tc;
  while (tc--) {
    int command;
    cin >> command;
    if (command == 0 && pq.empty()) {
      cout << "0\n";
      continue;
    }

    if (command == 0) {
      cout << pq.top() << endl;
      pq.pop();
    } else {
      pq.push(command);
    }
  }
}