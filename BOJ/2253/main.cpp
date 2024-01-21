#include <bits/stdc++.h>

using namespace std;

int n;
bool ban[10001];
int cache[200][10001];
const int INF = 98765432;

int dp(int point, int jump) {
    if (point > n || ban[point]) {
        return INF;
    }
    if (point == n) {
        return 0;
    }
    int& ret = cache[jump][point];
    if (ret != -1) {
        return ret;
    }
    ret = INF;
    int back, equal, next;
    
    equal = dp(point+jump, jump);
    next = dp(point+jump, jump+1);
    ret = min(equal, next);
    
    if (jump > 1) {
        back = dp(point+jump, jump-1);
        ret = min(back, ret);
    }
    return ++ret;
}

int main() {
    int m;
    cin >> n >> m;
    memset(cache, -1, sizeof(cache));
    
    for (int i = 0; i < m; i++) {
        int temp;
        cin >> temp;
        ban[temp] = true;
    }
    
    int ans = dp(1, 1);
    ans = ans < INF ? ans : -1;
    cout << ans;

    return 0;
}