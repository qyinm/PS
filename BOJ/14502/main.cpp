#include <iostream>
#include <queue>

using namespace std;

struct Dir {
    int x;
    int y;
};


int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
int arr[10][10];

int height, width;
queue<Dir> q_virus;


void bfs() {
    while(!q.empty()) {
        Dir cur = q.front();
        q.pop();

        Dir next;
        for (int i = 0; i < 4; i++) {

        }
    }
}
void wall() {

}
int main() {

    cin >> height >> width;

    for (int y = 1; y <= height; y++) {
        for (int x = 1; x <= width; x++) {
            cin >> arr[y][x];
        }
    }

    q.push({1, 1});
    visited[1][1];
    return 0;
}
