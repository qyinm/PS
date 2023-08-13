#include <cstdlib>
#include <iostream>
using namespace std;

int chess[15];

int n;
int Cnt = 0;

bool isValid(int row, int col) {
    for (int i = 1; i < row; i++) {
        if ((chess[i] == col) || (abs(row - i) == abs(col - chess[i]))) {
            return false;
        }
    }
    return true;
}
void queen(int row) {
    for (int col = 1; col <= n; col++) {
        chess[row] = col;
        if (isValid(row, col)) {
            if (row == n) {
                Cnt++;
                return;
            }
            queen(row + 1);
        }
    }
}
int main() {
    cin >> n;
    queen(1);

    cout << Cnt;
    return 0;
}