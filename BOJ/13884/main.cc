#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  int tc;
  cin >> tc;

  while (tc--) {
    int k, n;
    cin >> k >> n;

    vector<int> numbers(n);
    for (int i = 0; i < n; i++) {
      cin >> numbers[i];
    }
    vector<int> sorted_numbers = numbers;
    sort(sorted_numbers.begin(), sorted_numbers.end());

    int count = 0;
    int number_index = 0, sorted_index = 0;
    for (sorted_index = 0; sorted_index < n; sorted_index++) {
      while (number_index < n &&
             numbers[number_index++] != sorted_numbers[sorted_index]) {
        count += 1;
      }
    }
    cout << k << " " << count << endl;
  }

  return 0;
}