#include <iostream>
#include <vector>

std::vector<int> parents;
std::vector<int> count;

int find(int i) {
    
    int root, lead, tail;
    for (root = i; parents[root] >= 0; root = parents[root])
    ;

    for (tail = i; tail != root; tail = lead) {
        lead = parents[tail];
        parents[tail] = root;
    }
    return root;
}

void merge(int a, int b) {
    a = find(a);
    b = find(b);

    if (a == b) {
        return;
    }

    if (count[a] > count[b]) {
        parents[b] = a;
        count[a] += count[b];
    } else {
        parents[a] = b;
        count[b] += count[a];
    }

    return;
}

void printYesOrNo(int a, int b) {
    if (find(a) == find(b)) {
        std::cout << "YES\n";
    } else {
        std::cout << "NO\n";
    }
}

int main() {
    std::cin.tie(0);
    std::ios_base::sync_with_stdio(false);

    int n, m;

    std::cin >> n >> m;
    parents = std::vector<int>(n+1, -1);
    count = std::vector<int>(n+1, 1);

    int query, a, b;
    for (int i = 0; i < m; i++) {
        std::cin >> query >> a >> b;
        if (query == 0) {
            merge(a, b);
        } else if (query == 1) {
            printYesOrNo(a, b);
        }
    }

    return 0;
}