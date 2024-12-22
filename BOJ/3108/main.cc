#include <iostream>
#include <vector>

using namespace std;
using pii = pair<int, int>;
using rectangle = pair<pii, pii>;

bool isTouching(const rectangle& rect1, const rectangle& rect2) {
  const auto& [p1, p2] = rect1;  // rect1의 좌표
  const auto& [p3, p4] = rect2;  // rect2의 좌표

  bool inside = (p1.first < p3.first && p1.second < p3.second &&
                 p4.first < p2.first && p4.second < p2.second) ||
                (p3.first < p1.first && p3.second < p1.second &&
                 p2.first < p4.first && p2.second < p4.second);

  bool out = (p2.first < p3.first) || (p2.second < p3.second) ||
             (p4.first < p1.first) || (p4.second < p1.second);

  return inside || out;
}

void search(const int& current, const int& size,
            const vector<rectangle>& coordinations, vector<bool>& visited) {
  visited[current] = true;
  rectangle current_rectanble = coordinations[current];

  for (int i = 0; i < size; i++) {
    if (i == current) continue;
    if (visited[i]) continue;

    if (!isTouching(current_rectanble, coordinations[i])) {
      search(i, size, coordinations, visited);
    }
  }
}

int main() {
  cin.tie(0);
  std::ios_base::sync_with_stdio(false);

  int n, answer = -1;
  cin >> n;

  vector<rectangle> coordinations;  // 직사각형 좌표 저장
  coordinations.push_back({{0, 0}, {0, 0}});
  for (int i = 0; i < n; i++) {
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;

    rectangle current = {{x1, y1}, {x2, y2}};
    coordinations.push_back(current);  // 현재 직사각형 추가
  }
  vector<bool> visited(n + 1, false);
  for (int i = 0; i < n + 1; i++) {
    if (visited[i]) continue;
    answer++;
    search(i, n + 1, coordinations, visited);
  }

  cout << answer << endl;  // 결과 출력
  return 0;
}