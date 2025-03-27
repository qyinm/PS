#include <bits/stdc++.h>

using namespace std;

const char LEFT_CLOSE = '(';
const char RIGHT_CLOSE = ')';
const map<char, bool> char_to_bool = {{'T', true}, {'F', false}};
const map<bool, char> bool_to_char = {{true, 'T'}, {false, 'F'}};

int main() {
  int time = 1;
  while (true) {
    stack<char> st;
    string str;
    cin >> str;
    if (str == "()") break;

    int max_level = 0;
    int real_max_level = -1;
    for (const auto& ch : str) {
      if (ch == LEFT_CLOSE) max_level++;
      if (ch == RIGHT_CLOSE) max_level--;
      real_max_level = max(real_max_level, max_level);
    }
    // cout << real_max_level << endl;

    int level = 0;
    for (const auto& ch : str) {
      if (ch == RIGHT_CLOSE) {
        bool a = char_to_bool.at(st.top());
        st.pop();
        while (st.top() != LEFT_CLOSE) {
          bool op = char_to_bool.at(st.top());
          st.pop();
          if (level % 2 == real_max_level % 2) {
            a &= op;
          } else {
            a |= op;
          }
        }
        st.pop();
        st.push(bool_to_char.at(a));

        level -= 1;
        continue;
      }
      if (ch == LEFT_CLOSE) {
        level += 1;
      }
      st.push(ch);
    }

    printf("%d. %s\n", time, char_to_bool.at(st.top()) ? "true" : "false");
    time += 1;
  }
}
