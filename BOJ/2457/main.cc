#include <algorithm>
#include <iostream>
#include <vector>
#define FastIO cin.tie(0)->ios::sync_with_stdio(false);

using namespace std;

struct Flower {
  int start, end;
};

int main() {
  FastIO;

  int n;
  cin >> n;

  vector<Flower> flowers(n);
  for (int i = 0; i < n; i++) {
    int sm, sd, em, ed;
    cin >> sm >> sd >> em >> ed;
    int start = sm * 100 + sd;
    int end = em * 100 + ed;
    flowers[i] = {start, end};
  }

  sort(flowers.begin(), flowers.end(), [](auto &a, auto &b) {
    if (a.start == b.start) return a.end > b.end;
    return a.start < b.start;
  });

  int coverage = 301;
  int endDay = 1130;
  int idx = 0;
  int countFlower = 0;
  int maxEnd = 0;

  while (coverage <= endDay) {
    bool updated = false;

    while (idx < n && flowers[idx].start <= coverage) {
      if (maxEnd < flowers[idx].end) {
        maxEnd = flowers[idx].end;
      }
      idx++;
      updated = true;
    }

    if (!updated) {
      break;
    }

    coverage = maxEnd;
    countFlower++;

    if (maxEnd > endDay) {
      break;
    }
  }

  if (maxEnd <= endDay) {
    cout << 0 << "\n";
  } else {
    cout << countFlower << "\n";
  }

  return 0;
}