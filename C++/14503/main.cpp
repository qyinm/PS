#include <iostream>

using namespace std;

int dx[] = {0, 1, 0, -1};
int dy[] = {-1, 0, 1, 0};

int clean_area = 0;

int arr[50][50];
int n, m;

void dfs(int r_y, int r_x, int r_d) {


    int ny, nx;
    for (int i = 0; i < 4; i++) {
        if (r_d == 0) {
            r_d = 3;
        } else {
            r_d = (r_d - 1) % 4;
        }

        ny = r_y + dy[r_d];
        nx = r_x + dx[r_d];

        if (ny < 0 || ny >= n || nx < 0 || nx >= m) {
            continue;
        }

        if (arr[ny][nx] == 0) {
            clean_area++;
            arr[ny][nx] = -1; // 청소됨 -1이 매직넘버
            dfs(ny, nx, r_d);
        }
    }

    int bx = r_x - dx[r_d];
    int by = r_y - dy[r_d];
    if (!(bx < 0 || bx >= m || by < 0 || by >= n)&& arr[by][bx] != 1) {
        dfs(by, bx, r_d);
    } else {
        cout << clean_area;
        exit(0);
    }
}

int main() {
    int robot_y, robot_x, robot_dir;


    cin >> n >> m;
    cin >> robot_y >> robot_x >> robot_dir;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
        }
    }
    clean_area++;
    arr[robot_y][robot_x] = -1; // 청소됨 -1이 매직넘버
    dfs(robot_y, robot_x, robot_dir);
    cout << clean_area;

    return 0;
}
