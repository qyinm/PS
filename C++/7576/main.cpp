#include <iostream>
#include <queue>

using namespace std;

int N, M;
int visited[1001][1001];
int graph[1001][1001];
int tomatoMinDay;
int cycle;
int transitionTomatoCount;
queue<pair<int, int>> qu;

//void testDraw() {
//    for(int i = 1; i <= N; i++) {
//        for(int j = 1; j <= M; j++) {
//            cout << graph[i][j] << " ";
//        }
//        cout << endl;
//    }
//}

void bfs(int *dx, int *dy) {
    while (!qu.empty()) {
        cycle = qu.size();
        int transitionCount = 0;
        for (int i = 0; i < cycle; i++) {
            int y = qu.front().first;
            int x = qu.front().second;
            qu.pop();
            for (int j = 0; j < 4; j++) {
                int newY = y + dy[j];
                int newX = x + dx[j];
                if (graph[newY][newX] == 0 && !visited[newY][newX] && newY <= N && newY > 0 && newX <= M && newX > 0) {
                    qu.push(pair<int, int>(newY, newX));
                    visited[newY][newX] = 1;
                    graph[newY][newX] = 1;
                    transitionCount++;
                    transitionTomatoCount++;
                }
            }
        }
        if(!transitionCount)    break;
        tomatoMinDay++;
//        cout << tomatoMinDay << endl;
//        testDraw();
    }

}


int main() {
    int dx[] = {-1, 0, 1, 0};
    int dy[] = {0, 1, 0, -1};
    int boxCount = 0;
    cin >> M >> N;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            int tempTomato;
            cin >> tempTomato;
            graph[i][j] = tempTomato;
            if (tempTomato == 1) {
                qu.push(pair<int, int>(i, j));
                visited[i][j] = 1;
            }
            if (!tempTomato) {
                boxCount++;
            }
        }
    }


    bfs(dx, dy);
//    cout <<transitionTomatoCount << " " << boxCount << endl;
    if(boxCount == transitionTomatoCount) cout << tomatoMinDay;
    else    cout << -1;

    return 0;
}
