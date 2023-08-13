#include <iostream>
#include <algorithm>

using namespace std;

int cmp(const void *a, const void *b) {
    const int *x = (int *) a;
    const int *y = (int *) b;

    if (*x > *y)
        return 1;
    else if (*x < *y)
        return -1;
    return 0;
}

bool check[8][10001];
bool idxCheck[8];
int data[8];
int n, m;
int d[8];

void draw(int l) {
    for (int i = 0; i < l; i++) {
        cout << d[i] << " ";
    }
    cout << endl;
}

void solve(int len) {
    if (len == m) {
        draw(len);
        return;
    }
    for (int i = 0; i < n; i++) {
        if (!idxCheck[i] && !check[len][data[i]]) {
            idxCheck[i] = true;
            check[len][data[i]] = true;
            d[len] = data[i];
            solve(len + 1);
            idxCheck[i] = false;
        }
    }
    for (int j = 0; j < n; j++) {
        check[len][data[j]] = false;
    }
}

int main() {

    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        cin >> data[i];
    }
    sort(data, data+n);
    solve(0);
}