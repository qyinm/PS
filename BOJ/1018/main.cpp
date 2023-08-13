#include <iostream>

using namespace std;

int width, height;
int MIN = 100;
char colorB2W[] = {'B', 'W'};
char colorW2B[] = {'W', 'B'};

void solve(char chess[51][51], int y, int x) {
    for (int k = 0; k < 2; k++) {
        int cnt = 0;
        for (int i = 0; i < 8; i++) {
            int ny = y + i;
            for (int j = 0; j < 8; j++) {
                int nx = x + j;
                if ((i + j) % 2 == 0 && chess[ny][nx] == colorB2W[k]) {
                    cnt++;
                }
                if ((i + j) % 2 == 1 && chess[ny][nx] == colorW2B[k]) {
                    cnt++;
                }
            }
        }
        if (MIN > cnt) {
            MIN = cnt;
        }
    }
}

int main() {
    cin >> height >> width;
    char chess[51][51];
    for (int i = 0; i < height; i++) {
        cin >> chess[i];
    }

    for (int i = 0; i <= height - 8; i++) {
        for (int j = 0; j <= width - 8; j++) {
            solve(chess, i, j);
        }
    }
    cout << MIN;
}