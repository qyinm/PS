#include <iostream>
#include <cmath>

using namespace std;

void hanoi(int start, int end, int via, int n) {
    if(n==0){
        return;
    }
    hanoi(start, via, end, n-1);
    cout << start << " " << end << "\n";
    hanoi(via, end, start, n-1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int hanoi_height;
    cin >> hanoi_height;

    int hanoi_cycle = (int)pow(2, hanoi_height);
    hanoi_cycle--;
    cout << hanoi_cycle << "\n";
    hanoi(1,3,2,hanoi_height);
    return 0;
}
