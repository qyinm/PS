#include <iostream>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;

int N, M;
int answers[7];

void query(int level) {
  if (level == M) {
    for (int i = 0; i < M; i++) {
      cout << answers[i] << " ";
    }
    cout << "\n";
    return;
  }
  for (int i = 1; i <= N; i++) {
    answers[level] = i;
    query(level + 1);
  }
}

int main() {
  FastIO;

  cin >> N >> M;
  query(0);

  return 0;
}