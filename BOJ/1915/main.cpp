#include <iostream>
#include <stdio.h>
#include <queue>

using namespace std;

int arr[1001][1001];
int n;
int m;


void dp() {
    int ans = 0;
    for(int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (arr[i][j] == 0) continue;
            int val = min(arr[i-1][j-1], min(arr[i][j-1], arr[i-1][j]));
            arr[i][j] = ++val;
            ans = max(val, ans);
        }
    }
    cout << ans * ans << endl;
}

int main() {
    cin >> n >> m;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            scanf("%1d", &arr[i][j]);
        }
    }
    dp();
    return 0;
}
