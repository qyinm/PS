#include <bits/stdc++.h>

using namespace std;

int r, c, n, sw = 1;
vector<vector<char>> grid;
vector<int> sticks;

vector<int> dx = {-1, 0, 1, 0};
vector<int> dy = {0, 1, 0, -1};


pair<int, int> shootMineral(const int &height) {
    for (int i = 0; i < c; i++) {
        if (grid[height][i] == 'x') {
            return {i, height};
        }
    }
    return {-1, -1};
}

int bfs(int sx, int sy, vector<vector<int>> &visited) {
    queue<pair<int, int>> q;

    q.push({sx, sy});
    int curx, cury;
    while(!q.empty()) {
        int curx = q.front().first;
        int cury = q.front().second;
        q.pop();

        int nx, ny;
        for (int i = 0; i < 4; i++) {
            nx = curx + dx[i];
            ny = cury + dy[i];
            
            if (nx < 0 || nx >= c || ny < 0 || ny >= r) continue;
            if (visited[ny][nx] == 0 || grid[ny][nx] == '.')    continue;

            if (ny == 0) {
                return 1;
            }
            q.push({nx, ny});
            visited[ny][nx] = 1;
        }
    }
    return 0;

}


int main() {
    cin >> r >> c;

    grid.assign(r, vector<char>(c, 0));

    for (auto &row : grid) {
        for (auto &col : row) {
            cin >> col;
        }
    }
    
    cin >> n;
    sticks.assign(n, 0);
    for(auto &stick : sticks) {
        cin >> stick;
    }

    int posx, posy, nx, ny;
    for (auto const &stick: sticks) {
        auto shootMineralRet = shootMineral(stick);
        posx = shootMineralRet.first;
        posy = shootMineralRet.second;

        for (int i = 0; i < 4; i++) {
            vector<vector<int>> visited(100, vector<int>(100, 0));
            nx = posx + dx[i];
            ny = posy + dy[i];
            if (ny < 0 || ny >= c || nx < 0 || nx >= r) continue;
            if (grid[ny][nx] == '.')    continue;

            int checkLevitation = bfs(nx, ny, visited);
            if (!checkLevitation)    continue;
            
            vector<pair<int, int>> mineral_down;
            for (int h = 0; h < ny; h++) {
                for (int w = 0; w < c; w++) {
                    if (!visited[h][w])  continue;
                    mineral_down.push_back({w, h});
                }
                if (mineral_down.size() != 0)   break;
            }

            for (auto &mineral : mineral_down) {
                cout << mineral.first << mineral.second << endl;
            }
        }
    }

}