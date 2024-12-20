#include <iostream>

using namespace std;

vector<int> parents;

int find(int i) {
  int root, node, parent;
  for (root = i; parents[root] >= 0; root = parents[root]);
  for (node = i; node != root; node = parent) {
    parent = parents[node];
    parents[node] = root;
  }

  return root;
}

void unionFunc(int i, int j) {
  if (i == j) return;
  int sum_rank = parents[i] + parents[j];
  if (parents[i] <= parents[j]) {
    parents[i] = sum_rank;
    parents[j] = i;
  } else {
    parents[j] = sum_rank;
    parents[i] = j;
  }
}

int main() {
  cin.tie(0);
  std::ios_base::sync_with_stdio(false);

  int n, m, known_people_count;
  cin >> n >> m >> known_people_count;
  parents = vector<int>(n + 1, -1);
  vector<int> known_peoples(known_people_count);
  for (int i = 0; i < known_people_count; i++) {
    cin >> known_peoples[i];
  }
  for (int i = 1; i < known_people_count; i++) {
    unionFunc(find(known_peoples[i - 1]), find(known_peoples[i]));
  }

  int party_member_count;
  vector<vector<int>> parties;
  for (int i = 0; i < m; i++) {
    cin >> party_member_count;
    vector<int> members(party_member_count);
    for (auto& member : members) {
      cin >> member;
    }
    parties.push_back(members);
    for (int i = 1; i < party_member_count; i++) {
      unionFunc(find(members[i - 1]), find(members[i]));
    }
  }
  if (known_people_count == 0) {
    cout << m;
    return 0;
  }
  int answer = 0;
  for (const auto& party : parties) {
    bool flag = false;
    for (const auto& member : party) {
      if (find(member) == find(known_peoples[0])) {
        flag = true;
        break;
      }
    }
    if (!flag) {
      answer++;
    }
  }
  cout << answer;

  return 0;
}