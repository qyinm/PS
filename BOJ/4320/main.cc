#include <bits/stdc++.h>
#define FastIO cin.tie(NULL)->ios_base::sync_with_stdio(fasle);

using namespace std;
using ll = long long;

int main() {
  while (true) {
    ll x;
    cin >> x;
    if (x == 0) {
      break;
    }

    int mm = 1;
    int plli = sqrt(abs(x));
    int mili = -plli;

    int cur_p = 2;
    for (int p = 2; p <= 32; p++) {
      if (cur_p * cur_p == p) {
        cur_p = p;
        plli = sqrt(plli);
        mili = -plli;
      }
      //   cout << plli << " : " << mili << endl;
      for (int i = mili; i <= plli; i++) {
        ll temp = 1;
        for (int j = 1; j <= p; j++) {
          temp *= i;
        }
        if (temp == x) {
          mm = p;
          break;
        }
      }
    }
    cout << mm << "\n";
  }
}
