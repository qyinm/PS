#include <bits/stdc++.h>

using namespace std;

int r, c, n, sw = 1;
vector<vector<char>> grid;
vector<int> sticks;

vector<int> dx = {-1, 0, 1, 0};
vector<int> dy = {0, 1, 0, -1};


pair<int, int> shootMineral(const int &height) {
    if (sw == 1) {
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

int bfs(int sx, int sy, vector<vector<int>> &visited, priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> &clust) {
    queue<pair<int, int>> q;
    int chk = 0;
    q.push({sx, sy});
    visited[sy][sx] = 1;
    clust.push({sy, sx});
    int curx, cury;
    

    while(!q.empty()) {
        curx = q.front().first;
        cury = q.front().second;
        q.pop();

        int nx, ny;
        for (int i = 0; i < 4; i++) {
            nx = curx + dx[i];
            ny = cury + dy[i];
            
            if (nx < 0 || nx >= c || ny < 0 || ny >= r) continue;
            if (visited[ny][nx] == 1 || grid[ny][nx] == '.')    continue;

            if (ny == 0) {
                chk = 1;
            }
            q.push({nx, ny});
            visited[ny][nx] = 1;
            clust.push({ny, nx});
        }
    }
    return chk;

}


int main() {
    cin >> r >> c;

    grid.assign(r, vector<char>(c, 0));

    for (int i = r - 1; i >= 0; i--) {
        for (int j = c - 1; j >= 0; j--) {
            cin >> grid[i][j];
        }
    }
    cin >> n;
    sticks.assign(n, 0);
    for(auto &stick : sticks) {
        cin >> stick;
    }

    int posx, posy, nx, ny;
    for (auto const &stick: sticks) {
        auto shootMineralRet = shootMineral(stick - 1);
        sw *= -1;

        posx = shootMineralRet.first;
        posy = shootMineralRet.second;

        if (posx == -1 && posy == -1)   continue;
        
        for (int i = 0; i < 4; i++) {
            vector<vector<int>> visited(100, vector<int>(100, 0));
            nx = posx + dx[i];
            ny = posy + dy[i];
            if (ny < 0 || ny >= c || nx < 0 || nx >= r) continue;
            if (grid[ny][nx] == '.')    continue;

            priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> mineral_clust;
            int checkLevitation = bfs(nx, ny, visited, mineral_clust);
            if (checkLevitation)    continue;
            
            vector<pair<int, int>> mineral_down;


            for (int h = 0; h <= ny; h++) {
                for (int w = 0; w < c; w++) {
                    if (!visited[h][w])  continue;
                    mineral_down.push_back({h, w});
                }
                if (mineral_down.size() != 0)   break;
            }

            int minHeight = 2e9;
            for (const auto &mineral : mineral_down) {
                int height = mineral.first - 1;
                int curx = mineral.second;
                for (; grid[height][curx] != 'x'; height--);
                int curDistance = mineral.first - height - 1;
                minHeight = min(minHeight, curDistance);
            }
            
            while(!mineral_clust.empty()) {
                auto mineral = mineral_clust.top();
                int y = mineral.first;
                int x = mineral.second;
                mineral_clust.pop();

                grid[y][x] = '.';
                grid[y-minHeight][x] = 'x';
            }
            break;
        }
    }

    for (int i = r - 1; i >= 0; i--) {
        for (int j = c - 1; j >= 0; j--) {
            cout << grid[i][j];
        }
        cout << endl;
    }
}