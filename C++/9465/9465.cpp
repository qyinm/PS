#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;
        long long inVec[2][100002];
        long long dpV[2][100002];
        int tmp;
        for (int j = 0; j < n * 2; j++) {
            cin >> tmp;
            inVec[j / n][j % n] = tmp;
        }
        dpV[0][0] = inVec[0][0];
        dpV[1][0] = inVec[1][0];
        if (n == 1) {
            cout << max(dpV[0][0], dpV[1][0]) << endl;
            continue;
        }
        if (n > 1) {
            dpV[0][1] = inVec[0][1] + inVec[1][0];
            dpV[1][1] = inVec[1][1] + inVec[0][0];
        }
        for (int x = 2; x <= n; x++) {
            if (x == n) {
                cout << max(dpV[0][x - 1], dpV[1][x - 1]) << endl;
            }
            if (n > 2) {
                dpV[0][x] =
                    inVec[0][x] + max(dpV[0][x - 2] + inVec[1][x - 1],
                                      max(dpV[1][x - 2], dpV[1][x - 1]));
                dpV[1][x] =
                    inVec[1][x] + max(dpV[1][x - 2] + inVec[0][x - 1],
                                      max(dpV[0][x - 2], dpV[0][x - 1]));
            }
        }
    }
    return 0;
}