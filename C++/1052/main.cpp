#include <iostream>

using namespace std;
int solve(int n) {
    int cnt = 0;
    while (n != 0) {
        if (n & 1) {
            cnt++;
        }
        n >>= 1;
    }
    return cnt;
}
int main() {
    int n, k;
    cin >> n >> k;
    int ans = n;
    while (true) {
        if (solve(n) <= k) {
            ans = n - ans;
            break;
        }
        n++;
    }
    cout << ans;
}