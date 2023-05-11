#include<iostream>
#include<queue>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);
    int n;
    cin >> n;


    // 중앙값에서 작은 수들
    priority_queue<int> maxQ;
    // 중앙값에서 큰 수들    
    priority_queue<int, std::vector<int>, std::greater<int>> minQ;

    int temp;
    cin >> temp;
    maxQ.push(temp);
    cout << maxQ.top() << "\n";
    for (int i = 1; i < n; i++) {
        cin >> temp;

        if (i % 2 == 1) {
            if (maxQ.top() > temp) {
                minQ.push(maxQ.top());
                maxQ.pop();
                maxQ.push(temp);
            } else {
                minQ.push(temp);
            }
        } else {
            if (minQ.top() < temp) {
                maxQ.push(minQ.top());
                minQ.pop();
                minQ.push(temp);
            } else {
                maxQ.push(temp);
            }
        }

        cout << maxQ.top() << "\n";
    }

}