#include <cstdlib>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

struct Data {
    int left;
    int right;
    int cost;
};

vector<Data> v;
queue<Data> q;
void bruteforce(int n) {
    int cycle = q.size();
    for (int i = 0; i < cycle; i++) {
        int left = q.front().left;
        int right = q.front().right;
        int cost = q.front().cost;
        q.pop();

        q.push({n, right, cost + abs(left - n)});
        q.push({left, n, cost + abs(right - n)});

        v.push_back({n, right, cost + abs(left - n)});
        v.push_back({left, n, cost + abs(right - n)});
    }
}

int main() {
    int n;
    cin >> n;

    int b1, b2;
    cin >> b1 >> b2;

    v.push_back({b1, b2, 0});
    q.push({b1, b2, 0});
    int c;
    cin >> c;

    for (int i = 0; i < c; i++) {
        int temp;
        cin >> temp;
        bruteforce(temp);
    }

    int startIdx = 1;
    for (int i = 0; i < c; i++) {
        startIdx *= 2;
    }
    --startIdx;
    int min = 1000000000;
    for (int i = startIdx; i < v.size(); i++) {
        if (min > v[i].cost) {
            min = v[i].cost;
        }
    }
    cout << min << endl;
}