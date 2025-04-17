#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false);

using namespace std;
using ti = tuple<int, int, int>;

vector<vector<int>> board;
vector<vector<vector<int>>> memo;
vector<vector<ti>> weights = {
    {{1, 1, 1}, {0, 0, 1}}, 
    {{1, 1, 1}, {0, 0, 1}, {2, 1, 0}}, 
    {{1, 1, 1}, {2, 1, 0}}
};
int N;

int dp(int i, int j, int direction) {
    
    if (memo[direction][i][j] != -1) {
        return memo[direction][i][j];
    }
    if (i == (N-1) && j == (N-1)) {
        return 1;
    }
    
    memo[direction][i][j] = 0;
    int temp = 0;
    for (const auto& [nd, wy, wx] : weights[direction]) {
        int ny = i + wy;
        int nx = j + wx;

        if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
        if (board[ny][nx] != 0) continue;
        if (nd == 1 && (board[ny][j] != 0 || board[i][nx] != 0))  continue;
        temp += dp(ny, nx, nd);
        // cout << "i: " << i << " j: " << j << " memo: " << memo[i][j] << " " << ny << " " << nx << endl;
    }
    memo[direction][i][j] = temp;
    return memo[direction][i][j];
}

int main() {
    FastIO;
    cin >> N;
    memo.resize(N);
    for (auto& m : memo) {
        m.resize(N);
        for (auto& mm : m) {
            mm.resize(N, -1);
        }
    }
    board.resize(N);
    for (auto& b : board) {
        b.resize(N);
    }

    for (auto& row : board) {
        for (auto& el : row) {
            cin >> el;
        }
    }

    cout << dp(0, 1, 0) << endl;
}