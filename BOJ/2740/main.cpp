#include <iostream>
#include <vector>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;

int main() {
  FastIO;
  int n1, n2, m1, m2;

  cin >> n1 >> m1;
  vector<vector<int>> mat1(n1, vector<int>(m1));
  for (auto& row : mat1) {
    for (auto& e : row) {
      cin >> e;
    }
  }

  cin >> n2 >> m2;
  vector<vector<int>> mat2(n2, vector<int>(m2));
  for (auto& row : mat2) {
    for (auto& e : row) {
      cin >> e;
    }
  }

  int idx = 0;
  vector<vector<int>> ans(n1, vector<int>(m2));
  for (int i = 0; i < n1; i++) {
    for (int j = 0; j < m2; j++) {
      int sum = 0;
      for (int k = 0; k < m1; k++) {
        sum += mat1[i][k] * mat2[k][j];
      }
      ans[idx / m2][idx % m2] = sum;
      idx += 1;
    }
  }

  for (const auto& row : ans) {
    for (const auto& e : row) {
      cout << e << " ";
    }
    cout << "\n";
  }

  return 0;
}