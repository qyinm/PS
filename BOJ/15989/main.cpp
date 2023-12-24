#include <iostream>
#include <vector>

using namespace std;

int n;
vector<vector<int>> cache;

int dp(int num, int idx) {
    if (num < 0) {
        return 0;
    }
    if (num == 0) {
        return 1;
    }
    if (cache[idx][num] != -1) {
        return cache[idx][num];
    }
    cache[idx][num] = 0;
    for (int i = idx; i > 0; i--) {
        cache[idx][num] += dp(num - i, i);
    }
    return cache[idx][num];
}

int main() {
    
    int tc;
    cin >> tc;
    
    while (tc--) {
        int num;
        cin >> num;
        cache = vector<vector<int>>(4, vector<int>(10001, -1));
        int ans = dp(num, 3);
        cout << ans << "\n";
    }
    
    return 0;
}
