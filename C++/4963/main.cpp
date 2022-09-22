#include <iostream>
#include <queue>

using namespace std;

struct Dir {
    int x;
    int y;
};


int w, h = -1;
int island_count;
int graph[51][51];
int visited[51][51];
Dir dir[] = {{1,  0},
             {0,  1},
             {-1, 0},
             {0,  -1},
             {1,  1},
             {1,  -1},
             {-1, 1},
             {-1, -1},
};
queue<pair<int, int>> q;

void bfs() {
    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();

        for (auto &i: dir) {
            int next_x = x + i.x;
            int next_y = y + i.y;

            if (next_x < 1 || next_x > w || next_y < 1 || next_y > h) continue;
            if (!graph[next_y][next_x] || visited[next_y][next_x]) continue;

            q.push({next_y, next_x});
            visited[next_y][next_x] = 1;
        }
    }
}

void init() {
    island_count = 0;
    for (int i = 1; i < 51; i++) {
        for (int j = 1; j < 51; j++) {
            visited[i][j] = 0;
            graph[i][j] = 0;
        }
    }
}

int main() {

    while (1) {
        init();
        cin >> w >> h;
        if (!(w||h))    return 0;
        for (int i = 1; i <= h; i++) {
            for (int j = 1; j <= w; j++) {
                int temp_val;
                cin >> temp_val;
                graph[i][j] = temp_val;
            }
        }
        for (int i = 1; i <= h; i++) {
            for (int j = 1; j <= w; j++) {
                if (!visited[i][j] && graph[i][j]) {
                    q.push({i, j});
                    visited[i][j] = 1;
                    bfs();
                    island_count++;
                }
            }
        }
        cout << island_count << "\n";

    }
}
