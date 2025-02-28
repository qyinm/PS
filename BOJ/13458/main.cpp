#include <cmath>
#include <iostream>
#include <vector>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;

int main() {
  FastIO;
  long long n;
  cin >> n;
  vector<long long> students(n);
  for (auto& student : students) {
    cin >> student;
  }
  long long pri, sub;
  cin >> pri >> sub;

  long long ans = 0;
  for (const auto& student : students) {
    if (student == 0) continue;
    long long rest = student - pri;
    ans += 1;
    if (rest <= 0) continue;
    ans += ceil(rest / double(sub));
  }
  cout << ans;
  return 0;
}