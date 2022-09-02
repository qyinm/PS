#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int mi, ma;
    cin >> mi >> ma;
    vector<int> arr(ma + 1, false);
    for (int i = 1; i < arr.size(); i++) {
        if (i * i < ma + 1)
            arr[i * i] = true;
    }
    int ans_mi = 99999999, ans_sum = 0;
    for (int i = ma; i >= mi; i--) {
        if (arr[i]) {
            ans_mi = i;
            ans_sum += i;
        }
    }

    if (ans_sum) {
        cout << ans_sum << endl << ans_mi << endl;
    } else {
        cout << -1;
    }
}
