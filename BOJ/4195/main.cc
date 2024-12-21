#include <iostream>
#include <map>
#include <string>

using namespace std;

int find(int s, vector<int>& parents) {
  if (s == parents[s]) return s;
  return parents[s] = find(parents[s], parents);
}

void unionRank(int i, int j, vector<int>& parents, vector<int>& rank) {
  i = find(i, parents);
  j = find(j, parents);

  if (i == j) {
    cout << rank[i] << "\n";
    return;
  }

  int temp = rank[i] + rank[j];
  if (rank[i] > rank[j]) {
    rank[i] = temp;
    parents[j] = i;
  } else {
    rank[j] = temp;
    parents[i] = j;
  }

  cout << temp << "\n";
}

int main() {
  cin.tie(0);
  std::ios_base::sync_with_stdio(false);

  int tc, f;
  cin >> tc;

  while (tc--) {
    cin >> f;
    map<string, int> m;
    vector<int> parents(f * 2);
    vector<int> rank(f * 2, 1);
    int idx = 0;
    while (f--) {
      string a, b;
      cin >> a >> b;
      if (m.find(a) == m.end()) {
        m[a] = idx;
        parents[idx] = idx;
        idx += 1;
      }
      if (m.find(b) == m.end()) {
        m[b] = idx;
        parents[idx] = idx;
        idx += 1;
      }

      unionRank(m[a], m[b], parents, rank);
    }
  }

  return 0;
}