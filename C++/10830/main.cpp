#include<iostream>
#include<vector>
#include<map>

using namespace std;

int n;
map<long long int, vector<vector<int>>> dp;

vector<vector<int>> divisionSquares(vector<vector<int>> A, vector<vector<int>> B, long long int b);
vector<vector<int>> mergeSquares(vector<vector<int>> &A, long long int b);

int main() {    
    long long int b;
    cin >> n >> b;

    vector<vector<int>> arr(n, vector<int>(n));

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cin >> arr[i][j];
        }
    }
    dp[1] = arr;
    mergeSquares(arr, b);
    
    for(int i = 0; i < n; i++) {

        for(int j = 0; j < n; j++) {
            cout << dp[b][i][j] % 1000 << " ";
        }
        cout << "\n";
    }

    return 0;
}

vector<vector<int>> divisionSquares(vector<vector<int>> A, vector<vector<int>> B, long long int b) {
    vector<vector<int>> C(n, vector<int>(n, 0));


    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            for(int k = 0; k < n; k++) {
                C[i][j] = (((A[i][k] % 1000) * (B[k][j] % 1000)) % 1000 + (C[i][j] % 1000)) % 1000;
            }
        }
    }

    dp[b] = C;
    return dp[b];
}

vector<vector<int>> mergeSquares(vector<vector<int>> &A, long long int b) {
    if (dp.find(b) != dp.end()) {
        return dp[b];
    }
    if (b == 1) {
        return dp[1];
    } else if (b % 2 == 0) {
        return divisionSquares(mergeSquares(A, b / 2), mergeSquares(A, b / 2), b);
    } else if (b % 2 == 1) {
        return divisionSquares(mergeSquares(A, b / 2), mergeSquares(A, b / 2 + 1), b);
    }
}
