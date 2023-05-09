#include<iostream>
#include<queue>

using namespace std;

int main() {
    int n;
    cin >> n;


    // 중앙값에서 작은 수들
    priority_queue<int> maxQ;
    // 중앙값에서 큰 수들    
    priority_queue<int, std::vector<int>, std::greater<int>> minQ;

    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        
        if (i == 0) {
            maxQ.push(temp);
            cout << maxQ.top() << "\n";
            continue;
        }
        int tempq;
        if (i % 2 == 1) {
            if (maxQ.top() > temp) {
                tempq = maxQ.top();
                maxQ.pop();
                maxQ.push(temp);
                minQ.push(tempq);
            } else {
                minQ.push(temp);
            }
        } else {
            if (minQ.top() < temp) {
                tempq = minQ.top();
                minQ.pop();
                minQ.push(temp);
                maxQ.push(tempq);
            } else {
                maxQ.push(temp);
            }
        }

        cout << minQ.top() << "\n";

    }
}