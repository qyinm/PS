#include <iostream>
#include <list>
#include <vector>
#include <stack>

using namespace std;

void dfs(int current_node, vector<list<int>> &graph, stack<int> &cache,
         vector<int> &visited) {
  visited[current_node] = 1;
  for (const auto &next_node : graph[current_node]) {
    if (visited[next_node] == 2) continue;
    if (visited[next_node] == 1) {
      cout << 0 << endl;
      exit(0);
    }
    dfs(next_node, graph, cache, visited);
  }
  visited[current_node] = 2;
  cache.push(current_node);
}

int main() {
  int n, e;
  cin >> n >> e;
  vector<list<int>> graph(n + 1);

  while (e--) {
    int singer_count, singer, prev;
    cin >> singer_count >> singer;
    for (int i = 0; i < singer_count - 1; i++) {
      prev = singer;
      cin >> singer;
      graph[prev].push_back(singer);
    }
  }

  stack<int> cache;
  vector<int> visited(n + 1, 0);
  for (int i = 1; i < n + 1; i++) {
    if (visited[i] != 0) continue;
    dfs(i, graph, cache, visited);
  }

  while (!cache.empty()) {
    cout << cache.top() << endl;
    cache.pop();
  }
}