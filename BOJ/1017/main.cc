// #include <bits/stdc++.h>
// #define FastIO cin.tie(NULL)->ios_base::sync_with_stdio(false);

// using namespace std;

// int even_nums[50];
// int odd_nums[50];
// int match[50];
// int answer[50];
// bool visited[50];
// int odd_idx = 0;
// int even_idx = 0;
// int answer_idx = 0;
// int N;

// const bool isPrime[2001] = {
//     false, false, true,  true,  false, true,  false, true,  false, false,
//     false, true,  false, true,  false, true,  false, true,  false, false,
//     false, true, false, true,  false, true,  false, true,  true,  false,
//     false, true,  false, true,  false, false, false, true,  false, true,
//     false, false, false, true, false, true,  false, true,  false, true,
//     false, false, true,  false, true, false, true,  false, true,  true,
//     false, true,  false, true,  false, true, false, false, false, true,
//     false, true,  false, true,  false, false, true, false, true,  false,
//     true,  false, false, false, true,  false, false, true, false, true,
//     false, true,  true,  false, false, false, true,  false, true, false,
//     false, true,  false, false, false, true,  false, true,  false, true,
//     false, true,  true,  false, false, true,  false, true,  false, true,
//     false, true,  false, true,  true,  false, false, true,  false, false,
//     true,  false, true,  true,  false, true,  true,  false, true,  false,
//     true,  true,  false, true,  true,  true,  false, true,  true,  true,
//     false, true,  true,  false, true,  true,  true,  false, true,  true,
//     true,  false, true,  true,  true, false, true,  true,  true,  true, true,
//     true,  true,  true,  true,  true, false, true,  true,  true,  true, true,
//     true,  true,  false, true,  true, true,  false, true,  true,  true, true,
//     false, false, true,  true,  false, true,  false, true,  false, false,
//     false, true,  true,  true,  true,  true, true,  true,  true,  false,
//     true,  false, true,  false, true,  false, false, true,  true,  false,
//     true,  true,  true,  false, true,  true,  true,  true, true,  false,
//     true,  true,  false, true,  false, true,  true,  false, false, false,
//     true,  true,  false, true,  false, true,  true,  true,  true,  false,
//     true,  false, false, false, false, true,  true,  false, false};

// bool dfs(int curr) {
//   if (visited[curr]) {
//     return false;
//   }
//   visited[curr] = true;

//   for (int ei = 0; ei < even_idx; ei++) {
//     if (curr == 0) {
//       cout << "ei : " << ei << " " << "even: " << even_nums[ei]
//            << " odd_nums[curr] + even_nums[ei]: "
//            << odd_nums[curr] + even_nums[ei] << " " << match[ei] << "\n";
//     }
//     if (!isPrime[odd_nums[curr] + even_nums[ei]]) continue;
//     if (match[ei] == -1 || dfs(match[ei])) {
//       match[ei] = curr;
//       if (curr == 0) {
//         answer[answer_idx++] = even_nums[ei];
//       }
//       if (curr != 0) {
//         return true;
//       }
//     }
//   }
//   if (curr == 0) {
//     return true;
//   }
//   return false;
// }

// int main() {
//   cin >> N;

//   fill(match, match + 50, -1);
//   for (int i = 0; i < N; i++) {
//     int num;
//     cin >> num;
//     if (num % 2 == 0) {
//       even_nums[even_idx++] = num;
//     } else {
//       odd_nums[odd_idx++] = num;
//     }
//   }

//   for (int oi = odd_idx - 1; oi >= 0; oi--) {
//     fill(visited, visited + 50, false);
//     if (!dfs(oi)) {
//       cout << -1;
//       return 0;
//     }
//   }

//   for (int i = 0; i < answer_idx; i++) {
//     cout << answer[i] << " ";
//   }

//   return 0;
// }

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
      //   for (int m = 0; m < N; m++) {
      //     cout << match[m] << " ";
      //   }
      //   cout << "\n";
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