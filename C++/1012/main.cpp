#include <iostream>
#include <queue>

#define endl "\n"

using namespace std;

int graph[50][50];
bool bfs_visited[50][50];
int N, M;
int insects;
int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};
queue<pair<int, int>> q;

void bfs() {
    while(!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++) {
            int next_y = y + dy[i];
            int next_x = x + dx[i];

            if (next_y < 0 || next_y > N-1 || next_x < 0 || next_x > M-1) continue;
            if (graph[next_y][next_x] == 0 || bfs_visited[next_y][next_x]) continue;

            q.push({next_y, next_x});
            bfs_visited[next_y][next_x] = true;
        }

    }
}

void init() {
    insects = 0;
    for(int i = 0; i < 50; i++) {
        for (int j = 0; j < 50; j++) {
            graph[i][j] = 0;
            bfs_visited[i][j] = false;
        }
    }
}

int main() {
    int T;
    cin >> T;

    for (int t = 0; t < T; t++) {
        cin >> M >> N;
        int K;
        cin >> K;
        for (int k = 0; k < K; k++) {
            int x, y;
            cin >> x >> y;
            graph[y][x] = 1;
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if(graph[i][j] == 1 && !bfs_visited[i][j]) {
                    q.push({i, j});
                    bfs_visited[i][j] = true;
                    bfs();
                    insects+=1;
                }
            }
        }
        cout << insects << endl;
        init();
    }


    return 0;
}
