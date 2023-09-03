#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n;
int map[101][101];
vector<vector<bool>> visited;
int height;

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

void bfs(int y, int x) {
    queue<pair<int, int>> q;
    q.push({y, x});
    visited[y][x] = true;
    if (map[y][x] <= height)    return;
    while (!q.empty()) {
        int cy = q.front().first;
        int cx = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++) {
            int ny = cy + dy[i];
            int nx = cx + dx[i];

            if (ny < 0 || ny >= n || nx < 0 || nx >= n) continue;
            if (visited[ny][nx])   continue;
            visited[ny][nx] = true;
            if (map[ny][nx] <= height)  continue;
            q.push({ny, nx});
        }
    }
}

int main() {
    cin >> n;
    int maxH = -1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> map[i][j];
            maxH = max(maxH, map[i][j]);
        }
    }

    int answer = -1;
    for (int k = 0; k <= maxH; k++) {
        height = k;
        visited = vector<vector<bool>>(n, vector<bool>(n, false));
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j] || map[i][j] <= height)  continue;
                bfs(i, j);
                cnt++;
            }
        }
        answer = max(answer, cnt);
    }
    cout << answer << "\n";
}
