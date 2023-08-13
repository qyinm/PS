#include <iostream>
#include <queue>

#define endl "\n"

using namespace std;

int N, K, Hop;
int multiple[] = {1, 2, 1};
int add[] = {-1, 0, 1};
bool visited[100001];
int cycle;
queue<int> qu;

void bfs() {
    while (!qu.empty()) {
        cycle = qu.size();
        for(int i = 0; i < cycle; i++) {
            int cur = qu.front();
            qu.pop();
            if (cur == K) return;
            for (int j = 0; j < 3; j++) {
                int next_point = multiple[j] * cur + add[j];
                if (next_point < 0 || next_point > 100000 || visited[next_point]) continue;
                qu.push(next_point);
                visited[next_point] = true;
            }
        }
        Hop++;
    }
}

int main() {
    cin >> N >> K;
    qu.push(N);
    visited[N] = true;
    bfs();
    cout << Hop;
    return 0;
}
