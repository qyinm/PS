#include <iostream>
#include <cmath>

using namespace std;

int n, r, c;
int cnt;
int dx[] = {0, 1, -1, 1};
int dy[] = {0, 0, 1, 0};

void recur(int nCount, int x, int y) {
    if (nCount == 1) {
        for (int i = 0; i < 4; i++) {
            x += dx[i];
            y += dy[i];
            if (x == c && y == r) {
                cout << cnt;
            }
            cnt++;
        }
        return;
    }
    nCount--;
    int power = pow(2, nCount);
    if (x <= c && c < x + power && y <= r && r < y + power) {
        recur(nCount, x, y);
    }
    if (x + power <= c && c < x + 2 * power && y <= r && r < y + power) {
        cnt += pow(4, nCount);
        recur(nCount, x + power, y);
    }
    if (x <= c && c < x + power && y + power <= r && r < y + 2 * power) {
        cnt += pow(4, nCount) * 2;
        recur(nCount, x, y + power);
    }
    if (x + power <= c && c < x + 2 * power && y + power <= r && r < y + 2 * power) {
        cnt += pow(4, nCount) * 3;
        recur(nCount, x + power, y + power);
    }
}

int main() {
    cin >> n >> r >> c;
    recur(n, 0, 0);
    return 0;
}
