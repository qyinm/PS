#include <bits/stdc++.h>
#define FastIO cin.tie(NULL)->ios_base::sync_with_stdio(false);

using namespace std;

int nums[50];
bool visited[50];
int match[50];
int N;
vector<vector<int>> graph;

bool PRIME[2001];

void chey() {
  for (int i = 2; i <= 2000; i++) {
    if (PRIME[i]) continue;
    for (int j = i + i; j <= 2000; j += i) {
      PRIME[j] = true;
    }
  }
}

bool dfs(int curr, int fixed) {
  if (visited[curr]) {
    return false;
  }
  visited[curr] = true;

  for (const auto& next : graph[curr]) {
    if (next == fixed) continue;
    if (match[next] == -1 || dfs(match[next], fixed)) {
      match[next] = curr;
      return true;
    }
  }

  return false;
}

void END() {
  cout << "-1";
  exit(0);
}

int main() {
  FastIO;
  chey();
  cin >> N;

  int half = 0;

  for (int i = 0; i < N; i++) {
    cin >> nums[i];
    if (nums[i] % 2 == 0) half++;
  }

  if (half * 2 != N) {
    END();
  }

  graph.assign(N, vector<int>());
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (i == j) continue;
      if (!PRIME[nums[i] + nums[j]]) {
        graph[i].push_back(j);
      }
    }
  }

  vector<int> answer;
  for (const auto& fixed : graph[0]) {
    fill(match, match + 50, -1);
    match[fixed] = 0;
    bool flag = true;
    for (int i = 1; i < N; i++) {
      if ((nums[0] % 2) != (nums[i] % 2)) continue;
      fill(visited, visited + 50, false);
      if (!dfs(i, fixed)) {
        flag = false;
      }
    }
    if (flag) {
      answer.push_back(nums[fixed]);
    }
  }
  if (answer.size() == 0) {
    END();
  }

  sort(answer.begin(), answer.end());
  for (const auto& a : answer) {
    cout << a << " ";
  }

  return 0;
}