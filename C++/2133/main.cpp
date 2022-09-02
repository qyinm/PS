#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    int arr[31] = {1, 0, 3};

    for(int i = 3; i < 31; i++) {
        if(i%2==1){
            arr[i] = 0;
            continue;
        }
        int sum = 3*arr[i-2];
        for(int j = i; j > 3; j--){
            sum += 2*arr[j-4];
        }
        arr[i] += sum;
    }
    cout << arr[n];
    return 0;
}
