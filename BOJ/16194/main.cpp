#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false)

using namespace std;

int main() {
  FastIO;
  int N;
  cin >> N;

  vector<int> cards(N + 1);
  for (int i = 1; i <= N; i++) {
    cin >> cards[i];
  }

  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= i / 2; j++) {
      cards[i] = min(cards[i], cards[j] + cards[i - j]);
    }
  }
  cout << cards[N];
}