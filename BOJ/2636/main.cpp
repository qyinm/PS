#include <iostream>
#include <queue>

#define endl "\n"
using namespace std;

struct Dir {
    int x;
    int y;
};

int cheese[101][101];
int width, height;
bool visited[101][101];
int dx[] = {-1, 0, 1, 0};
int dy[] = {0, -1, 0, 1};
queue<Dir> q;

int bfs() {
    int cnt = 0;
    while (!q.empty()) {
        int x = q.front().x;
        int y = q.front().y;
        q.pop();
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 1 || nx > width || ny < 1 || ny > height)
                continue;
            if (cheese[ny][nx] == 0 && visited[ny][nx] == 0) {
                q.push({nx, ny});
                visited[ny][nx] = true;
            }
            if (cheese[ny][nx] == 1 && visited[ny][nx] == 0) {
                visited[ny][nx] = true;
                cheese[ny][nx] = 0;
                cnt++;
            }
        }
    }
    return cnt;
}

void init() {
    for (int i = 1; i <= height; i++) {
        for (int j = 1; j <= width; j++) {
            visited[i][j] = false;
        }
    }
}

int main() {
    cin >> height >> width;
    int ans_cnt = 0;
    int t = 0;
    for (int i = 1; i <= height; i++) {
        for (int j = 1; j <= width; j++) {
            int temp;
            cin >> temp;
            cheese[i][j] = temp;
        }
    }

    while (true) {
        q.push({1, 1});
        visited[1][1] = true;
        int new_cnt = bfs();
        if (new_cnt == 0) {
            break;
        }
        t++;
        ans_cnt = new_cnt;
        init();
    }

    cout << t << endl << ans_cnt;
    return 0;
}
