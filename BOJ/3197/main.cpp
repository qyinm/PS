#include <iostream>
#include <queue>

using namespace std;

string hosu[1500];

queue<pair<int, int>> water_q;
pair<int, int> swan[2];

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};
int r, c;

void bfs_swan() {
    vector<vector<int>> swan_visited(r, vector<int>(c, 0));
    queue<pair<int, int>> swan_q;
    queue<pair<int, int>> next_swan_q;
    swan_q.push({swan[0].first, swan[0].second});
    int day = 0;
    while (!water_q.empty()) {
        while (!swan_q.empty()) {
            int y = swan_q.front().first;
            int x = swan_q.front().second;
            swan_q.pop();
            if (y == swan[1].first && x == swan[1].second) {
                cout << day;
                exit(0);
            }

            int ny;
            int nx;
            for (int i = 0; i < 4; ++i) {
                ny = y + dy[i];
                nx = x + dx[i];

                if ((nx < 0 || nx >= c || ny >= r || ny < 0)) continue;
                if (swan_visited[ny][nx]) continue;
                if (hosu[ny][nx] == 'X') {
                    next_swan_q.push({ny, nx});
                    swan_visited[ny][nx] = 1;
                } else {
                    swan_q.push({ny, nx});
                    swan_visited[ny][nx] = 1;
                }
            }
        }
        swan_q = next_swan_q;
        while (!next_swan_q.empty()) {
            next_swan_q.pop();
        }

        int size = water_q.size();
        for (int s = 0; s < size; ++s) {

            int y = water_q.front().first;
            int x = water_q.front().second;

            water_q.pop();

            int ny;
            int nx;
            for (int i = 0; i < 4; ++i) {
                ny = y + dy[i];
                nx = x + dx[i];

                if ((nx < 0 || nx >= c || ny >= r || ny < 0)) continue;
                if (hosu[ny][nx] == 'X') {
                    water_q.push({ny, nx});
                    hosu[ny][nx] = '.';
                }
            }
        }
        day++;
    }
}

int main() {
    cin >> r >> c;
    vector<vector<int>> vis(r, vector<int>(c, 0));
    int swan_idx = 0;
    for (int i = 0; i < r; i++) {
        cin >> hosu[i];
        for (int j = 0; j < c; j++) {
            if (hosu[i][j] == 'L') {
                hosu[i][j] = '.';
                swan[swan_idx++] = {i, j};
            }
            if (hosu[i][j] == '.') {
                for (int k = 0; k < 4; k++) {
                    int nx = j + dx[k];
                    int ny = i + dy[k];
                    if ((nx >= 0 && nx < c && ny >= 0 && ny < r) && hosu[ny][nx] == 'X' && !vis[i][j]) {
                        water_q.push({i, j});
                        vis[i][j] = 1;
                    }
                }
            }
        }
    }

    bfs_swan();
}