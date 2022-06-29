#include <iostream>
#include <algorithm>
#include <vector>
#define INF 1000000001
using namespace std;
vector <int> minTree;
vector <int> maxTree;
vector <int> Array;

int minInit(int start, int end, int node) {
    if(start == end) {
        return minTree[node] = Array[start];
    }
    int mid = (start + end) / 2;

    return minTree[node] = min(minInit(start, mid, node * 2), minInit(mid + 1, end, node * 2 + 1));
}

int maxInit(int start, int end, int node) {
    if(start == end) {
        return maxTree[node] = Array[start];
    }
    int mid = (start + end) / 2;

    return maxTree[node] = max(maxInit(start, mid, node * 2), maxInit(mid + 1, end, node * 2 + 1));
}

int minFind(int start, int end, int left, int right, int node) {
    if(right < start || left > end) {
        return INF;
    }
    if(end <= right && left <= start){
        return minTree[node];
    }
    int mid = (start + end) / 2;
    return min(minFind(start, mid, left, right, node * 2), minFind(mid + 1, end, left, right, node * 2 + 1));
}

int maxFind(int start, int end, int left, int right, int node) {
    if(right < start || left > end) {
        return -INF;
    }
    if(end <= right && left <= start){
        return maxTree[node];
    }
    int mid = (start + end) / 2;
    return max(maxFind(start, mid, left, right, node * 2), maxFind(mid + 1, end, left, right, node * 2 + 1));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, m;
    cin >> n >> m;
    for(int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        Array.push_back(temp);
    }

    minTree.resize(n * 4);
    maxTree.resize(n * 4);
    maxInit(0, n-1, 1);
    minInit(0, n-1, 1);

    for(int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        int mmax = maxFind(0, n-1, a-1, b-1, 1);
        int mmin = minFind(0, n-1, a-1, b-1, 1);
        cout << mmin << " " << mmax << '\n';
    }
}