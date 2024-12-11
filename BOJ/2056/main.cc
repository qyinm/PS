#include <iostream>
#include <vector>
#include <list>
#include <stack>

using namespace std;
using pil = pair<int, vector<int>>;

int main() {
  int n;
  cin >> n;

  vector<pil> graph(n + 1);
  vector<int> costs(n + 1);
  vector<int> answer(n + 1);
  stack<int> st;
  for (int i = 1; i < n + 1; i++) {
    int cost, preprocess_count;
    cin >> cost >> preprocess_count;
    costs[i] = cost;
    graph[i].first = preprocess_count;

    if (preprocess_count == 0)  {
      st.push(i);
      answer[i] = cost;
    }

    for (int j = 0; j < preprocess_count; j++) {
      int preprocess;
      cin >> preprocess;
      graph[preprocess].second.push_back(i);
    }
  }

  while (!st.empty()) {
    int current_node = st.top();
    st.pop();

    for (auto next_node : graph[current_node].second) {
      answer[next_node] = max(answer[next_node], answer[current_node] + costs[next_node]);
      graph[next_node].first -= 1;
      if (graph[next_node].first == 0) {
        st.push(next_node);
      }
    }
  }

  int a = -1;
  for (int ans : answer) {
    a = max(a, ans);
  }
  cout << a;
}