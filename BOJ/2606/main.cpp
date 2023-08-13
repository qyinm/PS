#include<iostream>
#include<queue>

using namespace std;

bool graph[101][101];   // 그래프끼리의 연결
bool bfs_visited[101];  // 해당 노드의 감염여부
int nodes, edges;
int virus_count;        // 바이러스 개수
queue<int> q;

void bfs() {
    while(!q.empty()) {
        int cur_node = q.front();
        q.pop();

        for (int node = 1; node <= nodes; node++) {
            if (bfs_visited[node] || !graph[cur_node][node]) {  // 해당 노드가 이미 감염되었거나, 현재노드와 연결되어 있지 않았다면 continue
                continue;
            }
            q.push(node);
            bfs_visited[node] = true;
            virus_count++;
        }
    }
}

int main(void) {
    cin >> nodes >> edges;

    for (int edge = 0; edge < edges; edge++) {
        int node_1, node_2;
        cin >> node_1 >> node_2;
        graph[node_1][node_2] = true;
        graph[node_2][node_1] = true;
    }
    q.push(1);
    bfs_visited[1] = true;

    bfs();

    cout << virus_count << endl;
}