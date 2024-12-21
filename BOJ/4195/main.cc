#include <iostream>
#include <map>
#include <string>

using namespace std;

string find(const string s, map<string, string>& m) {
  if (s == m[s]) return s;
  return m[s] = find(m[s], m);
}

void unionRank(string i, string j, map<string, string>& m,
               map<string, int>& rank) {
  int temp = rank[i] + rank[j];
  if (rank[i] < rank[j]) {
    rank[i] = temp;
    m[j] = i;
  } else {
    rank[j] = temp;
    m[i] = j;
  }
}

int main() {
  cin.tie(0);
  std::ios_base::sync_with_stdio(false);

  int tc, f;
  cin >> tc;

  while (tc--) {
    cin >> f;
    map<string, string> m;
    map<string, int> rank;
    while (f--) {
      string a, b;
      cin >> a >> b;
      if (m.find(a) == m.end()) {
        m[a] = a;
        rank[a] = -1;
      }
      if (m.find(b) == m.end()) {
        m[b] = b;
        rank[b] = -1;
      }
      m[a] = find(a, m);
      m[b] = find(b, m);
      if (m[a] != m[b]) {
        unionRank(m[a], m[b], m, rank);
      }
      cout << -min(rank[m[a]], rank[m[b]]) << "\n";
    }
  }

  return 0;
}