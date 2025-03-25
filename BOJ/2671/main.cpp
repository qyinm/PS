#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false)

using namespace std;

enum State { S0, S1, S2, S3, S4, S5, S6, S7, S8, Se };
map<State, map<int, State>> transitions = {
    {S0, {{1, S1}, {0, S7}}}, {S1, {{1, Se}, {0, S2}}},
    {S2, {{1, Se}, {0, S3}}}, {S3, {{1, S4}, {0, S3}}},
    {S4, {{1, S5}, {0, S7}}}, {S5, {{1, S4}, {0, S6}}},
    {S6, {{0, S3}, {1, S8}}}, {S7, {{1, S8}, {0, Se}}},
    {S8, {{1, S1}, {0, S7}}}};

State current_state = S0;
set<State> final_states = {S4, S5, S8};

int main() {
  FastIO;
  string str;
  cin >> str;

  string output = "SUBMARINE";
  for (auto s : str) {
    int input_data = (int)(s - '0');
    current_state = transitions[current_state][input_data];
    if (current_state == Se) {
      break;
    }
  }
  if (final_states.find(current_state) == final_states.end()) {
    output = "NOISE";
  }

  cout << output;
  return 0;
}