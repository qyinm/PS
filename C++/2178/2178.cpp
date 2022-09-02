#include <algorithm>
#include <iostream>
#include <queue>
#include <string>
#include <vector>

using namespace std;

int main() {
    int n, m;

    string miro[101];
    int dist[101][101];
    bool check[101][101];

    cin >> n >> m;
    queue<pair<int, int>> Q;

    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, 1, 0, -1};

    for (int i = 0; i < n; i++) {
        cin >> miro[i];
    }

    dist[0][0] = 1;
    Q.push({0, 0});
    check[0][0] = 1;

    while (!Q.empty()) {

        pair<int, int> cur = Q.front();
        Q.pop();

        for (int dir = 0; dir < 4; dir++) {
            int nx = cur.first + dx[dir];
            int ny = cur.second + dy[dir];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                continue;

            if (miro[nx][ny] == '0' || check[nx][ny])
                continue;

            dist[nx][ny] = dist[cur.first][cur.second] + 1;
            Q.push({nx, ny});
            check[nx][ny] = 1;
        }
    }

    cout << dist[n - 1][m - 1];

    return 0;
}
