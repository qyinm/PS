#include <iostream>
#include <vector>

using namespace std;

struct Node {
  int indegree;
  vector<int> edges;
};

void topology(int n, vector<Node> graph, vector<int> build_time) {
  vector<int> least_time(n + 1, 0);
  int top = -1;
  for (int i = 1; i < n + 1; i++) {
    if (graph[i].indegree == 0) {
      graph[i].indegree = top;
      top = i;
    }
  }

  for (int i = 0; i < n; i++) {
    int current_node = top;
    top = graph[top].indegree;
    least_time[current_node] += build_time[current_node];
    for (const auto& to : graph[current_node].edges) {
      least_time[to] = max(least_time[to], least_time[current_node]);
      graph[to].indegree -= 1;
      if (graph[to].indegree == 0) {
        graph[to].indegree = top;
        top = to;
      }
    }
  }

  for (int i = 1; i < n + 1; i++) {
    cout << least_time[i] << "\n";
  }
}

int main() {
  int n;
  cin >> n;
  vector<Node> graph(n + 1);
  vector<int> build_time(n + 1);

  for (int i = 1; i < n + 1; i++) {
    int time, to;
    cin >> time;
    build_time[i] = time;
    while (true) {
      cin >> to;
      if (to == -1) {
        break;
      }
      graph[to].edges.push_back(i);
      graph[i].indegree += 1;
    }
  }
  
  topology(n, graph, build_time);

  return 0;
}