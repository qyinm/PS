#include <cmath>
#include <iostream>
#include <string>

using namespace std;

int numLen(int num) {
    int len = 0;
    int i, j;
    for (i = 1, j = 1; i * 10 <= num; i *= 10, ++j) {
        len += 9 * i * j;
    }
    len += (num - i + 1) * j;
    return len;
}

int binarySearch(int left, int right, int key) {
    if (left >= right) {
        return right;
    }
    int mid = (left + right) / 2;
    int midLen = numLen(mid);
    if (midLen < key) {
        return binarySearch(mid + 1, right, key);
    } else {
        return binarySearch(left, mid, key);
    }
}

int main() {
    int n, k;

    cin >> n >> k;

    if (numLen(n) < k) {
        cout << -1;
        return 0;
    }
    int num = binarySearch(1, n, k);
    int n_len = numLen(num);
    string num_s = to_string(num);

    cout << num_s[num_s.size() - 1 - (n_len - k)];
    return 0;
}