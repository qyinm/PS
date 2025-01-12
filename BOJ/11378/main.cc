#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;

struct Node {
  int link_count;
  vector<int> links;
};

bool cmp(Node a, Node b) { return a.link_count > b.link_count; }

int N, M, K;
bool visited[1001];
vector<Node> graph;
int matched[1001];

bool bimatch(int worker) {
  for (const auto& job : graph[worker].links) {
    if (visited[job]) continue;
    visited[job] = true;
    if (matched[job] == -1 || bimatch(matched[job])) {
      matched[job] = worker;
      return true;
    }
  }

  return false;
}

int main() {
  FastIO;
  cin >> N >> M >> K;
  graph = vector<Node>(N);
  memset(matched, -1, sizeof(matched));

  for (auto& node : graph) {
    cin >> node.link_count;
    node.links = vector<int>(node.link_count);

    for (auto& link : node.links) {
      cin >> link;
    }
  }
  sort(graph.begin(), graph.end(), cmp);

  int answer = 0;
  for (int i = 0; i < N; i++) {
    memset(visited, false, sizeof(visited));
    if (bimatch(i)) {
      answer++;
    }
  }

  for (int i = 0; i < N; i++) {
    while (K > 0) {
      memset(visited, false, sizeof(visited));
      if (!bimatch(i)) {
        break;
      }
      answer++;
      K -= 1;
    }
  }

  cout << answer;

  return 0;
}