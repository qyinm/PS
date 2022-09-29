#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int Min[2000001];
    vector<int> v;
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        v.push_back(temp);
    }
    sort(v.begin(), v.end());
    int cnt;
    vector<bool> temp(v.size(), false);
    for (int r = 1; r <= n; r++) {
        for (int i = 0; i < r; i++)
            temp[i] = true;
        do {
            int cnt = 0;
            for (int i = 0; i < v.size(); ++i) {
                if (temp[i] == true)
                    cnt += v[i];
            }
            Min[cnt] = 1;
        } while (prev_permutation(temp.begin(), temp.end()));
    }
    for (int i = 1; i < 2000001; i++) {
        if (Min[i] == 0) {
            cout << i << endl;
            break;
        }
    }
    return 0;
}