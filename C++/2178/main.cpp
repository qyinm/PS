#include <iostream>
#include <queue>

using namespace std;

int N, M;
int graph[101][101];
int bfs_visited[101][101];
int cost[101][101];

int dx[] = {0, 1, 0, -1};
int dy[] = { 1, 0, -1, 0};

queue<pair<int, int>> q;

void bfs() {
    while (!q.empty()) {
        int column = q.front().first;
        int row = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int next_column = column + dy[i];
            int next_row = row + dx[i];
            if (next_column < 1 || next_column > N || next_row < 1 || next_row > M) {
                continue;
            }
            if (!graph[next_column][next_row] || bfs_visited[next_column][next_row]) {
                continue;
            }
            q.push({next_column, next_row});
            bfs_visited[next_column][next_row] = 1;
            cost[next_column][next_row] = cost[column][row] + 1;
        }
    }
}

int main() {

    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;
    for (int col = 1; col <= N; col++) {
        for (int row = 1; row <= M; row++) {
            int temp;
            scanf("%1d", &temp);
            graph[col][row] = temp;
        }
    }
    q.push({1, 1});
    bfs_visited[1][1] = 1;
    cost[1][1] = 1;
    bfs();
    cout << cost[N][M];
    return 0;
}
