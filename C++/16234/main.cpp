#include <iostream>
#include <cmath>
#include <queue>

using namespace std;

typedef struct point {
    int x;
    int y;
} point;

int n, l, r;
int arr[51][51];
int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

queue<point> q;
vector<point> changePoint;

bool check(int &a, int &b) {
    int dif = abs(a - b);
    return dif <= r && dif >= l;
}

int s;
int c;
int visited[51][51];
int flag;

void bfs() {
    while (!q.empty()) {
        int x = q.front().x;
        int y = q.front().y;
        q.pop();

        s += arr[y][x];
        c += 1;
        int nx, ny;
        for (int i = 0; i < 4; i++) {
            nx = x + dx[i];
            ny = y + dy[i];
            if (nx > n || nx < 1 || ny > n || ny < 1) continue;
            if (visited[ny][nx]) continue;
            if (check(arr[y][x], arr[ny][nx])) {
                flag = 1;
                q.push({nx, ny});
                visited[ny][nx] = 1;
                changePoint.push_back({nx, ny});
            }
        }
    }
}

void changeVal() {
    int val = s / c;
    for (const auto &point: changePoint) {
        arr[point.y][point.x] = val;
    }
}

int main() {
    cin >> n >> l >> r;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cin >> arr[i][j];
        }
    }

    int day = 0;
    while (true) {
        flag = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (visited[i][j]) continue;
                q.push({j, i});
                visited[i][j] = 1;
                changePoint.push_back({j, i});
                bfs();
                changeVal();
                changePoint.clear();
                c ^= c;
                s ^= s;
            }
        }
        memset(visited, 0, sizeof(visited));
        if (!flag) {
            cout << day;
            break;
        }
        day++;
    }

    return 0;
}
