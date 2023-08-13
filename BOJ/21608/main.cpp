#include <iostream>
#include <queue>

using namespace std;

int n;
int cnt1 = -1;
int cnt2 = -1;
int py;
int px;
int ans = 0;

int dx[] = {0, -1, 0, 1};
int dy[] = {1, 0, -1, 0};

void count(vector<vector<int>> &mx, const vector<vector<int>> &student, int val) {
    for (int y = 1; y <= n; y++) {
        for (int x = 1; x <= n; x++) {
            if (mx[y][x]) continue;

            int cn1 = 0;
            int cn2 = 0;
            int nx, ny;
            for (int d = 0; d < 4; d++) {
                nx = x + dx[d];
                ny = y + dy[d];

                if (nx < 1 || nx > n || ny < 1 || ny > n) continue;
                if (!mx[ny][nx]) {
                    cn2++;
                    continue;
                }
                for (const auto &fr: student[val]) {
                    if (mx[ny][nx] == fr) {
                        cn1++;
                        break;
                    }
                }
            }
            if (cn1 > cnt1) {
                px = x;
                py = y;
                cnt1 = cn1;
                cnt2 = cn2;
            } else if (cn1 == cnt1) {
                if (cn2 > cnt2) {
                    px = x;
                    py = y;
                    cnt1 = cn1;
                    cnt2 = cn2;
                }
            }
        }
    }
    mx[py][px] = val;

    cnt1 = -1;
    cnt2 = -1;
}

void solve() {
    cin >> n;
    vector<vector<int>> mx(n + 1, vector<int>(n + 1, 0));


    vector<vector<int>> student(n * n + 1);

    for (int i = 1; i <= n * n; i++) {
        int val;
        cin >> val;
        for (int j = 0; j < 4; j++) {
            int temp;
            cin >> temp;
            student[val].push_back(temp);
        }
        count(mx, student, val);
    }

    for (int y = 1; y <= n; y++) {
        int cnt;
        for (int x = 1; x <= n; x++) {
            int nx, ny;
            cnt = 0;
            for (int d = 0; d < 4; d++) {
                nx = x + dx[d];
                ny = y + dy[d];

                if (nx < 1 || nx > n || ny < 1 || ny > n) continue;

                for (const auto &bf: student[mx[y][x]]) {
                    if (mx[ny][nx] == bf) {
                        cnt++;
                        break;
                    }
                }
            }
            switch (cnt) {
                case 0:
                    ans += 0;
                    break;
                case 1:
                    ans += 1;
                    break;
                case 2:
                    ans += 10;
                    break;
                case 3:
                    ans += 100;
                    break;
                case 4:
                    ans += 1000;
                    break;
            }
        }
    }

    cout << ans;
}

int main() {
    solve();
    return 0;
}
