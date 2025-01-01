#include <bits/stdc++.h>
#define FastIO std::cin.tie(NULL)->ios_base::sync_with_stdio(false);

using namespace std;
using Row = vector<char>;
using Floor = vector<Row>;
using Building = vector<Floor>;
using Point = tuple<int, int, int>;
using ll = long long;
using Node = pair<ll, Point>;

vector<Point> weights = {{1, 0, 0},  {-1, 0, 0}, {0, 1, 0},
                         {0, -1, 0}, {0, 0, 1},  {0, 0, -1}};

int n, r, c;

bool invalidPoint(const Point& point) {
  auto [x, y, z] = point;

  return (x < 0 || x >= n || y < 0 || y >= r || z < 0 || z >= c);
}

int search(const Building& building, const Point& start, const Point& end) {
  priority_queue<Node, vector<Node>, greater<>> pq;
  vector<vector<vector<ll>>> cost(n, vector<vector<ll>>(r, vector<ll>(c, 1e9)));
  cost[get<0>(start)][get<1>(start)][get<2>(start)] = 0;
  pq.push({0, start});

  while (!pq.empty()) {
    auto current_cost = pq.top().first;
    auto current_point = pq.top().second;
    auto [current_x, current_y, current_z] = current_point;
    pq.pop();

    if (current_point == end) return current_cost;

    for (const auto& weight : weights) {
      Point next_point = {current_x + get<0>(weight),
                          current_y + get<1>(weight),
                          current_z + get<2>(weight)};
      auto [next_x, next_y, next_z] = next_point;
      if (invalidPoint(next_point) || building[next_x][next_y][next_z] == '#')
        continue;
      if (cost[next_x][next_y][next_z] > current_cost + 1) {
        cost[next_x][next_y][next_z] = current_cost + 1;
        pq.push({current_cost + 1, next_point});
      }
    }
  }
  return -1;
}

void solve() {
  Building building = Building(n, Floor(r, Row(c)));
  Point startPoint, endPoint;

  string dumb;
  string data;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < r; j++) {
      cin >> data;
      for (int k = 0; k < c; k++) {
        building[i][j][k] = data.at(k);
        if (building[i][j][k] == 'S') {
          startPoint = {i, j, k};
        } else if (building[i][j][k] == 'E') {
          endPoint = {i, j, k};
        }
      }
    }
  }

  auto answer = search(building, startPoint, endPoint);
  if (answer == -1) {
    printf("Trapped!\n");
  } else {
    printf("Escaped in %lld minute(s).\n", answer);
  }
}

int main() {
  FastIO;

  Building graph;
  while (true) {
    cin >> n >> r >> c;
    if (n == 0) break;
    solve();
  }

  return 0;
}