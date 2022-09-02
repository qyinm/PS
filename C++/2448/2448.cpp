#include <iostream>
#include <vector>
using namespace std;

void star(int x, int y, int n, vector<vector<char>> &s) {
    if (n == 3) {
        s[y][x + 2] = '*';
        s[y + 1][x + 1] = '*';
        s[y + 1][x + 3] = '*';
        s[y + 2][x] = '*';
        s[y + 2][x + 1] = '*';
        s[y + 2][x + 2] = '*';
        s[y + 2][x + 3] = '*';
        s[y + 2][x + 4] = '*';
        return;
    } else {
        star(x + n / 2, y, n / 2, s);
        star(x, y + n / 2, n / 2, s);
        star(x + n, y + n / 2, n / 2, s);
    }
}

int main() {
    int n;
    cin >> n;

    vector<vector<char>> s(n, vector<char>(n * 2, ' '));
    star(0, 0, n, s);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n * 2; j++) {
            cout << s[i][j];
        }
        cout << endl;
    }
    return 0;
}
