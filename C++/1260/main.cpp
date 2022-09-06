#include <iostream>
#include <stack>
#include <queue>

using namespace std;

int tree[1001][1001];
int bfs_visited[1001];
int dfs_visited[1001];
int vertex_num;
int edge_num;
int start_vertex;

queue<int> qu;

void bfs() {
    if (qu.size() == 0) {
        return;
    }
    int start = qu.front();
    qu.pop();
    cout << start << " ";
    for (int i = 1; i <= vertex_num; i++) {
        if (tree[start][i] == 1 && !bfs_visited[i]) {
            bfs_visited[i] = 1;
            qu.push(i);
        }
    }
    bfs();
}

void dfs(int vertex) {
    if (dfs_visited[vertex]) {
        return;
    }
    dfs_visited[vertex]= 1;
    cout << vertex << " ";
    for (int i = 1; i <= vertex_num; i++) {
        if (tree[vertex][i] == 1 && !dfs_visited[i]) {
            dfs(i);
        }
    }
}

int main() {
    cin >> vertex_num >> edge_num >> start_vertex;
    for (int i = 0; i < edge_num; i++) {
        int a, b;
        cin >> a >> b;
        tree[a][b] = 1;
        tree[b][a] = 1;
    }
    dfs(start_vertex);
    cout << endl;
    qu.push(start_vertex);
    bfs_visited[start_vertex] = 1;
    bfs();
    return 0;
}
