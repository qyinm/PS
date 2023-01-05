#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> data(n);
    vector<int> cache(n);
    for (auto &d: data) {
        cin >> d;
    }

    cache[n - 1] = 1;
    int ans = 1;
    for (int i = n - 2; i >= 0; i--) {
        int maxL = 0;
        for (int j = i + 1; j < n; j++) {
            if (data[i] < data[j]) {
                maxL = max(cache[j], maxL);
            }
        }
        cache[i] = maxL + 1;
        ans = max(cache[i], ans);
    }
    cout << ans;

    return 0;
}
