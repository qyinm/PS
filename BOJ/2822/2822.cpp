#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

bool cmp(pair<int, int> a, pair<int, int> b) { return a.second > b.second; }

int main() {
    map<int, int> ans;
    for (int i = 0; i < 8; i++) {
        int t;
        cin >> t;
        ans[i + 1] = t;
    }

    vector<pair<int, int>> sortByValue(ans.begin(), ans.end());
    sort(sortByValue.begin(), sortByValue.end(), cmp);
    vector<int> temp;
    int sum = 0;
    int tempCount = 0;
    auto it = sortByValue.begin();
    for (auto it = sortByValue.begin(); tempCount < 5; it++) {
        sum += it->second;
        temp.push_back(it->first);
        tempCount++;
    }
    cout << sum << endl;
    sort(temp.begin(), temp.end());
    for (int i = 0; i < 5; i++) {
        cout << temp[i] << endl;
    }
    return 0;
}
