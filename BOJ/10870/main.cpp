#include <iostream>
using namespace std;

int fibonachi(int n) {
    if (!n)  return 0;
    if (n == 1) return 1;
    return fibonachi(n-1) + fibonachi(n-2);
}
int main() {
    int n;
    cin >> n;
    cout << fibonachi(n);
    return 0;
}
