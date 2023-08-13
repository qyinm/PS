#include <iostream>

using namespace std;

int main() {
    int len;
    int play1, play2;

    cin >> len >> play1 >> play2;

    int distance = 2;
    int cnt = 1;
    while (1) {
        for (int i = 1; i <= len; i += distance) {
            if (i <= play1 && play1 <= i + distance - 1 && i <= play2 && play2 <= i + distance - 1) {
                printf("%d", cnt);
                return 0;
            }
        }
        distance *= 2;
        cnt++;
    }
}