#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;



int main() {


    int n;
    cin >> n;
    vector<int> data;
    data.push_back(0);

    for (int i = 1; i <= n; i++) {
        int temp;
        cin >> temp;

        if (temp > data.back()) {
            data.push_back(temp);
        } else {
            auto p = upper_bound(data.begin(), data.end(), temp);
            *p = temp;
        }
    }
    cout << data.size() - 1;

    return 0;
}
