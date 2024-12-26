#include <iostream>
#include <vector>

using namespace std;

vector<int> parents;

int find(int i) {
  if (parents[i] < 0) return i;
  return parents[i] = find(parents[i]);
}

bool union_node(int a, int b) {
  a = find(a);
  b = find(b);

  if (a == b) return true;

  if (parents[a] < parents[b]) {
    parents[a] += parents[b];
    parents[b] = a;
  } else {
    parents[b] += parents[a];
    parents[a] = b;
  }

  return false;
}

int main() {
  cin.tie(0);
  std::ios_base::sync_with_stdio(false);
  int n, m;
  cin >> n >> m;

  parents = vector<int>(n, -1);
  int answer = 0;
  for (int i = 1; i <= m; i++) {
    int a, b;
    cin >> a >> b;
    if (union_node(a, b)) {
      answer = i;
      break;
    }
  }
  cout << answer;
}