#include <cmath>
#include <iostream>
#include <queue>

using namespace std;
using pdd = pair<double, double>;

int canMove(pdd from, pdd to) {
  int dist_x = abs(to.first - from.first);
  int dist_y = abs(to.second - from.second);

  int needBear = ceil((dist_x + dist_y) / (double)50);
  return needBear <= 20;
}

bool bfs(const vector<pdd>& points) {
  vector<bool> visited(points.size(), false);
  queue<pdd> q;
  q.push(points[0]);
  visited[0] = true;

  while (!q.empty()) {
    auto current_point = q.front();
    q.pop();

    for (int i = 0; i < points.size(); i++) {
      if (visited[i]) continue;
      if (canMove(current_point, points[i])) {
        visited[i] = true;
        q.push(points[i]);
      }
    }
  }

  return visited[points.size() - 1];
}

void solve() {
  int store_count;
  cin >> store_count;

  vector<pdd> points(2 + store_count);
  for (auto& point : points) {
    double x, y;
    cin >> x >> y;
    point = {x, y};
  }

  if (bfs(points)) {
    cout << "happy\n";
  } else {
    cout << "sad\n";
  }
}

int main() {
  int tc;
  cin >> tc;

  while (tc--) {
    solve();
  }
}