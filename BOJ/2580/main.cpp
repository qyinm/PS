#include <iostream>
#include <vector>

using namespace std;

struct point {
    int y;
    int x;
};
int sudoku[9][9];
vector<point> v;

void draw() {
    for (auto &i: sudoku) {
        for (int j: i) {
            cout << j << " ";
        }
        cout << "\n";
    }
}

int isValid(int val, int x, int y) {

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (sudoku[(y / 3) * 3 + i][(x / 3) * 3 + j] == val || sudoku[i * 3 + j][x] == val ||
                sudoku[y][i * 3 + j] == val) {
                return false;
            }
        }
    }
    return true;
}

int flag;

void solve(int p) {
    if (p == v.size()) {
        flag = 1;
        return;
    }
    int x = v[p].x;
    int y = v[p].y;
    for (int i = 1; i <= 9; i++) {
        if (isValid(i, x, y)) {
            sudoku[y][x] = i;
            solve(p + 1);
        }
    }
    if (!flag) {
        sudoku[y][x] = 0;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            int temp;
            cin >> temp;
            sudoku[i][j] = temp;
            if (!temp) {
                v.push_back({i, j});
            }
        }
    }

    solve(0);
    draw();
    return 0;
}