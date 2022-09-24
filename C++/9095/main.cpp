#include <iostream>

using namespace std;

int recursion(int n) {
    if (n == 1)
        return 1;
    if (n == 2)
        return 2;
    if (n == 3)
        return 4;

    return recursion(n - 1) + recursion(n - 2) + recursion(n - 3);
}

int main() {
    int cycle;
    cin >> cycle;

    for (int i = 0; i < cycle; i++) {
        int temp;
        cin >> temp;
        cout << recursion(temp) << endl;
    }
}