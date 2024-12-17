#include <iostream>
#include <set>

using namespace std;

int main() {
    set<string> s;
    int n, m;

    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        string value;
        cin >> value;
        s.insert(value);
    }

    int cnt = 0;
    for (int i = 0; i < m; i++) {
        string find_value;
        cin >> find_value;
        auto it = s.find(find_value);

        if (it != s.end())  cnt++;
    }

    cout << cnt;
}