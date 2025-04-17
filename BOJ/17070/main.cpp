#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false)
using namespace std;

int n;
vector<vector<int>> board;
vector<vector<vector<int>>> dp;

// 각 방향에서 가능한 다음 상태들 (다음방향, dy, dx)
const vector<vector<tuple<int,int,int>>> next_state = {
    {{0,0,1}, {1,1,1}},           // 가로
    {{0,0,1}, {1,1,1}, {2,1,0}},  // 대각
    {{1,1,1}, {2,1,0}}            // 세로
};

int solve(int y, int x, int dir) {
    if (y == n-1 && x == n-1) return 1;
    
    int& ret = dp[dir][y][x];
    if (ret != -1) return ret;
    
    ret = 0;
    for (auto [ndir, dy, dx] : next_state[dir]) {
        int ny = y + dy;
        int nx = x + dx;
        
        if (ny >= n || nx >= n || board[ny][nx]) continue;
        if (ndir == 1 && (board[ny][x] || board[y][nx])) continue;
        
        ret += solve(ny, nx, ndir);
    }
    return ret;
}

int main() {
    FastIO;
    
    cin >> n;
    board.resize(n, vector<int>(n));
    dp.resize(3, vector<vector<int>>(n, vector<int>(n, -1)));
    
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> board[i][j];
            
    cout << solve(0, 1, 0) << '\n';
    
    return 0;
}