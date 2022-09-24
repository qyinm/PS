#include <iostream>

using namespace std;

struct Data {
    int t;
    int p;
};

Data arr[100];
int recursive(int s, int n) {

    if (s + arr[s].t - 1 >= n) {
        return 0;
    }
    int v = 0;
    for (int i = s; i < n; i++) {
        int temp = arr[s].p + recursive(arr[s].t + i, n);
        if (temp > v)
            v = temp;
    }
    return v;
}

int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i].t;
        cin >> arr[i].p;
    }
    int max = -1;
    for (int i = 0; i < n; i++) {

        int temp = recursive(i, n);
        if (temp > max) {
            max = temp;
        }
    }
    cout << max;
    return 0;
}