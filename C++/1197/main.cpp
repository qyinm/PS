#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef struct edges {
    int s;
    int e;
    int w;
} edges;

int v, e;
int cnt, ans;

bool cmp(edges &a, edges &b) {
    if (a.w < b.w) {
        return true;
    }
    return false;
}

int findParent(int x, vector<int> &parent) {
    if (parent[x] == x) {
        return x;
    }
    return parent[x] = findParent(parent[x], parent);
}

void unionParent(edges ev, vector<int> &parent) {
    int pi = findParent(ev.s, parent);
    int pj = findParent(ev.e, parent);
    if (pi == pj)   return;
    ans += ev.w;
    parent[pi] = pj;
    cnt++;
}

int main() {
    cin >> v >> e;

    vector<edges> edgeV(e);
    vector<int> parent(v + 1);
    for (int i = 1; i <= v; i++) {
        parent[i] = i;
    }

    for (auto &ev: edgeV) {
        cin >> ev.s >> ev.e >> ev.w;
    }

    sort(edgeV.begin(), edgeV.end(), cmp);

    for (auto ev: edgeV) {
        unionParent(ev, parent);
        if (cnt == v - 1)    break;
    }
    cout << ans << "\n";
    return 0;
}
