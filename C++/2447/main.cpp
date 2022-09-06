#include <iostream>

using namespace std;
char arr[10000][10000];
int patternN;

void tri_recursion(int x, int y, int n) {
    if (n == 1) {
        arr[y][x] = '*';
    } else {
        n /= 3;
        tri_recursion(x, y, n);
        tri_recursion(x + n, y, n);
        tri_recursion(x + n + n, y, n);
        tri_recursion(x, y + n, n);
        tri_recursion(x + n + n, y + n, n);
        tri_recursion(x, y + n + n, n);
        tri_recursion(x + n, y + n + n, n);
        tri_recursion(x + n + n, y + n + n, n);
    }
}

void drawing() {
    for (int i = 0; i < patternN; i++) {
        for (int j = 0; j < patternN; j++) {
            if(!arr[i][j]){
                cout<<" ";
                continue;
            }
            cout << arr[i][j];
        }
        cout << endl;
    }
}

int main() {
    cin >> patternN;
    tri_recursion(0,0,patternN);
    drawing();
    return 0;
}
