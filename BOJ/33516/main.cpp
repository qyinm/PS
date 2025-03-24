#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;

int main() {
  FastIO;
  int N;
  cin >> N;

  vector<char> skeep = {'s', 'k', 'e', 'e', 'p'};
  stack<char> st;
  int ans = 0;
  for (int i = 0; i < N; i++) {
    char ch;
    cin >> ch;
    st.push(ch);

    while (st.size() >= 5) {
      stack<char> temp;

      bool flag = true;
      for (int i = 4; i >= 0; i--) {
        if ((i == 0 && st.top() != skeep[i]) ||
            (st.top() != '*' && st.top() != skeep[i])) {
          flag = false;
          break;
        }
        temp.push(st.top());
        st.pop();
      }
      if (!flag) {
        while (!temp.empty()) {
          st.push(temp.top());
          temp.pop();
        }
        break;
      } else {
        st.push('*');
        ans += 1;
      }
    }
  }
  cout << ans;
}