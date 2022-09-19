#include <iostream>
#include <queue>

using namespace std;

queue<int> q;
int Node, Edge;
int Sets;
int graph[1001][1001];
int visited[1001];

void bfs() {
    Sets++;
    while(!q.empty()) {
        int y = q.front();
        q.pop();
        for(int i = 1; i <= Node; i++) {
            if(visited[i] || graph[y][i]==0) continue;
            q.push(i);
            visited[i] = true;
        }
    }
}

int main() {
    cin >> Node >> Edge;

    for (int e = 0; e < Edge; e++) {
        int x, y;
        cin >> x >> y;
        graph[x][y] = 1;
        graph[y][x] = 1;
    }

    for (int ny = 1; ny <= Node; ny++) {
        for (int nx = 1; nx <= Node; nx++) {
            if (!visited[ny]) {
                q.push(ny);
                visited[ny] = true;
                bfs();
            }
        }
    }

    cout << Sets;
    return 0;
}
