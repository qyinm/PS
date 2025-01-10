#include <iostream>

using namespace std;

int day_count[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
string days[] = {"MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"};

int main() {
  int x, y;
  cin >> x >> y;
  int diff_day = 0;
  for (int i = 1; i < x; i++) {
    diff_day += day_count[i];
  }
  diff_day += y - 1;
  diff_day %= 7;

  cout << days[diff_day];

  return 0;
}