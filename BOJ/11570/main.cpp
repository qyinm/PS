#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 2001;
int n;
vector<int> arr;
int memo[MAX_N][MAX_N];

int dp(int last1, int last2, int idx) {
    if (idx == n) {
        return 0;
    }
    
    if (memo[last1 + 1][last2 + 1] != -1) {
        return memo[last1 + 1][last2 + 1];
    }
    
    int curr = arr[idx];
    int cost1, cost2;
    
    if (last1 == -1) {
        cost1 = 0;
    } else {
        cost1 = abs(arr[last1] - curr);
    }
    
    if (last2 == -1) {
        cost2 = 0;
    } else {
        cost2 = abs(arr[last2] - curr);
    }
    
    // 두 가지 옵션 중 최소값 선택
    return memo[last1 + 1][last2 + 1] = min(
        dp(idx, last2, idx + 1) + cost1,
        dp(last1, idx, idx + 1) + cost2 
    );
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    cin >> n;
    arr.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    memset(memo, -1, sizeof(memo));
    
    cout << dp(-1, -1, 0) << '\n';
    
    return 0;
}