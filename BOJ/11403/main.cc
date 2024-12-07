#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<vector<int>> vec(n, vector<int>(n, 0));

    for (auto& v : vec) {
        int val;
        for (int i = 0; i < n; i++) {
            cin >> val;
            v[i] = val;
        }
    }

    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (vec[i][j] == 0 && vec[i][k] + vec[k][j] == 2) {
                    vec[i][j] = 1;
                }
            }
        }
    }

    for (const auto& ve: vec) {
        for (const auto& v: ve) {
            cout << v << " ";
        }
        cout << "\n";
    }

    return 0;
}