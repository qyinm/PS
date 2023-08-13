#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> data(n);
    vector<int> cache(n, 1);
    for (auto &d: data) {
        cin >> d;
    }

    int ans = 0;
    for (int i = n - 1; i >= 0; i--) {
        for (int j = i + 1; j < n; j++) {
            if (data[i] < data[j]) cache[i] = max(cache[j] + 1, cache[i]);
        }
        ans = max(cache[i], ans);
    }
    cout << ans;

    return 0;
}
