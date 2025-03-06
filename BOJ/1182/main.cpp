#include <bits/stdc++.h>

using namespace std;

int N, S;
vector<int> vec;

int cnt;
void func(vector<int>& sum, int index) {
  int s = 0;
  for (const auto& ss : sum) {
    s += ss;
  }
  if (sum.size() > 0 && s == S) {
    cnt++;
  }
  if (index == N) {
    return;
  }
  for (int i = index; i < N; i++) {
    sum.push_back(vec[i]);
    func(sum, i + 1);
    sum.pop_back();
  }
}

int main() {
  cin >> N >> S;
  vec.resize(N);
  for (auto& v : vec) {
    cin >> v;
  }
  vector<int> sum;
  func(sum, 0);
  cout << cnt;
}