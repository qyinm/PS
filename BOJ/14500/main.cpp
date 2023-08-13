#include <iostream>

using namespace std;
int n, m;
int maxNum;

int arr[501][501];
int square[3][2] = {{0, 1}, {1, 0}, {1, 1}};
int twist[4][3][2] = {{{1, 0}, {1, 1}, {2, 1}},
                      {{1, 0}, {1, -1}, {2, -1}},
                      {{0, 1}, {1, 1}, {1, 2}},
                      {{0, 1}, {1 , 0}, {1, -1}},
};
int L[4][2] = {{2, 1}, {0, 1}, {0, -1}, {2, -1}};
int fuck[2][2] = {{1, 1}, {1, -1}};

bool validPoint(int y, int x) {
    return (y < 0 || y >= n || x < 0 || x >= m);
}

void updateMaxNum(int num) {
    maxNum = num >= maxNum ? num : maxNum;
}

void searchSquare() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int num = arr[i][j];
            for (int k = 0; k < 3; k++) {
                int ny = i + square[k][0];
                int nx = j + square[k][1];
                if (validPoint(ny, nx)) {
                    num = 0;
                    break;
                }
                num += arr[ny][nx];
            }
            updateMaxNum(num);
        }
    }
}


void searchLFuckStick() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int num = arr[i][j];
            for (int k = 1; k < 3; k++) {
                if (validPoint(i + k, j)){
                    num = 0;
                    break;
                }
                num += arr[i + k][j];
            }
            int add = 0;
            for (auto & k : L) {
                if (validPoint(i + k[0], j + k[1])) {
                    continue;
                }
                add = add < arr[i + k[0]][j + k[1]] ? arr[i + k[0]][j + k[1]] : add;
            }
            for (auto & k : fuck) {
                if (validPoint(i + k[0], j + k[1])) {
                    continue;
                }
                add = add < arr[i + k[0]][j + k[1]] ? arr[i + k[0]][j + k[1]] : add;
            }
            if (!validPoint(i + 3, j)) {
                add = add < arr[i + 3][j] ? arr[i + 3][j] : add;
            }
            num += add;
            updateMaxNum(num);
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int num = arr[i][j];
            for (int k = 1; k < 3; k++) {
                if (validPoint(i, j + k)){
                    num = 0;
                    break;
                }
                num += arr[i][j + k];
            }
            int add = 0;
            for (auto & k : L) {
                if (validPoint(i + k[1], j + k[0])) {
                    continue;
                }
                add = add > arr[i + k[1]][j + k[0]] ? add : arr[i + k[1]][j + k[0]];
            }
            for (auto & k : fuck) {
                if (validPoint(i + k[1], j + k[0])) {
                    continue;
                }
                add = add > arr[i + k[1]][j + k[0]] ? add : arr[i + k[1]][j + k[0]];
            }
            if (!validPoint(i, j+3)) {
                add = add > arr[i][j + 3] ? add : arr[i][j +3];
            }
            num += add;
            updateMaxNum(num);
        }
    }
}

void searchTwist() {
    for (int c = 0; c < 4; c++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int num = arr[i][j];
                for (int k = 0; k < 3; k++) {
                    int ny = i + twist[c][k][0];
                    int nx = j + twist[c][k][1];
                    if (validPoint(ny, nx)) {
                        num = 0;
                        break;
                    }
                    num += arr[ny][nx];
                }
                updateMaxNum(num);
            }
        }
    }
}


int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
        }
    }
    searchSquare();
    searchTwist();
    searchLFuckStick();
    cout << maxNum;
    return 0;
}
