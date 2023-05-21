#include <iostream>
#include <queue>
#include <set>
#include <vector>

using namespace std;

int r, c, n, sw = 1;
char grid[100][100];
vector<int> sticks;

vector<int> dx = {-1, 0, 1, 0};
vector<int> dy = {0, 1, 0, -1};

void printGrid() {
    for (int i = r - 1; i >= 0; i--) {
        for (int j = 0; j < c; j++) {
            cout << grid[i][j];
        }
        cout << endl;
    }
}

pair<int, int> shootMineral(const int &height, int &nn) {
    if (nn % 2 == 0) {
        for (int i = 0; i < c; i++) {
            if (grid[height][i] == 'x') {
                grid[height][i] = '.';
                return {i, height};
            }
        }
    } else {
        for (int i = c - 1; i >= 0; i--) {
            if (grid[height][i] == 'x') {
                grid[height][i] = '.';
                return {i, height};
            }
        }
    }
    return {-1, -1};
}

int bfs(int sx, int sy, vector<vector<int>> &visited,
        multiset<pair<int, int>> &clust) {
    queue<pair<int, int>> q;
    int chk = 0;
    q.push({sx, sy});
    visited[sy][sx] = 1;
    clust.insert({sy, sx});
    int curx, cury;

    while (!q.empty()) {
        curx = q.front().first;
        cury = q.front().second;
        q.pop();

        int nx, ny;
        for (int i = 0; i < 4; i++) {
            nx = curx + dx[i];
            ny = cury + dy[i];

            if (nx < 0 || nx >= c || ny < 0 || ny >= r)
                continue;
            if (visited[ny][nx] == 1 || grid[ny][nx] == '.')
                continue;

            if (ny == 0) {
                chk = 1;
            }
            q.push({nx, ny});
            visited[ny][nx] = 1;
            clust.insert({ny, nx});
        }
    }
    return chk;
}

int main() {
    cin >> r >> c;

    for (int i = r - 1; i >= 0; i--) {
        for (int j = 0; j < c; j++) {
            cin >> grid[i][j];
        }
    }
    cin >> n;

    int posx, posy, nx, ny, stick;
    for (int nn = 0; nn < n; nn++) {
        cin >> stick;
        // printGrid();
        auto shootMineralRet = shootMineral(stick - 1, nn);
        // printGrid();
        posx = shootMineralRet.first;
        posy = shootMineralRet.second;

        if (posx == -1 || posy == -1)
            continue;

        for (int i = 0; i < 4; i++) {
            vector<vector<int>> visited(100, vector<int>(100));
            nx = posx + dx[i];
            ny = posy + dy[i];
            if (ny < 0 || ny >= r || nx < 0 || nx >= c)
                continue;
            if (grid[ny][nx] == '.')
                continue;

            multiset<pair<int, int>> mineral_clust;
            int checkLevitation = bfs(nx, ny, visited, mineral_clust);
            if (checkLevitation)
                continue;

            int minHeight = 987654321;
            for (auto &mineral : mineral_clust) {
                int cnt = 0;
                for (int height = mineral.first - 1; height >= 0; height--) {
                    if (grid[height][mineral.second] == '.')
                        cnt++;
                    if (grid[height][mineral.second] == 'x' &&
                        visited[height][mineral.second] == 0) {
                        break;
                    }
                }
                minHeight = min(minHeight, cnt);
            }

            for (auto &mineral : mineral_clust) {
                int y = mineral.first;
                int x = mineral.second;

                grid[y][x] = '.';
                grid[y - minHeight][x] = 'x';
            }
        }
    }

    printGrid();
}