#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int virus = 0;
int tree[200][200];
int visited[200];
queue<int> q;
int vertex_num;

void bfs() {
    if (q.size() == 0) return;
    int start = q.front();
    q.pop();
    for (int i = 1; i <= vertex_num; i++) {
        if (tree[start][i] == 1 && !visited[i]) {
            q.push(i);
            virus++;
            visited[i] = 1;
        }
    }
    bfs();
}

int main() {
    int edges_num;

    cin >> vertex_num;
    cin >> edges_num;


    for (int i = 0; i < edges_num; i++) {
        int a, b;
        cin >> a >> b;
        tree[a][b] = 1;
        tree[b][a] = 1;
    }
    q.push(1);
    visited[1] = 1;
    bfs();
    cout << virus;
    return 0;
}