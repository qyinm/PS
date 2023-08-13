#include <iostream>
#include <queue>

using namespace std;

int N;
int bfs_visited[1001];
int dfs_visited[1001];
int graph[1001][1001];
queue<int> q;

void dfs(int point) {
    cout << point << " ";

    for (int i = 1; i <= N; i++) {
        if (graph[point][i] == 1 && dfs_visited[i] == 0) {
            dfs_visited[i] = 1;
            dfs(i);
        }
    }
}

void bfs() {
    while (!q.empty()) {
        int point = q.front();
        q.pop();
        cout << point << " ";
        for (int i = 1; i <= N; i++) {
            if (graph[point][i] == 1 && bfs_visited[i] == 0) {
                q.push(i);
                bfs_visited[i] = 1;
            }
        }
    }
}

int main() {
    int edge, startPoint;

    cin >> N >> edge >> startPoint;

    for (int i = 0; i < edge; i++) {
        int a, b;
        cin >> a >> b;
        graph[a][b] = 1;
        graph[b][a] = 1;
    }
    dfs_visited[startPoint] = 1;
    dfs(startPoint);

    printf("\n");

    q.push(startPoint);
    bfs_visited[startPoint] = 1;
    bfs();

    return 0;
}