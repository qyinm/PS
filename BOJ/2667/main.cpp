#include <iostream>
#include <queue>

using namespace std;

queue<pair<int, int>> q;
int graph[26][26];
bool visited[26][26];
int map_size;
int apartment[1001];
int apartment_count;
int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};

void swap(int *a, int *b) {
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

void sort(int n) {
    for(int i = 0; i < n-1; i++) {
        int min = i;
        for(int j = i+1; j < n; j++) {
            if(apartment[min] > apartment[j])   min = j;
        }
        swap(apartment[min], apartment[i]);
    }
}

void bfs(){
    while(!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();
        apartment_count++;
        for(int i = 0; i < 4; i++) {
            int next_y = y + dy[i];
            int next_x = x + dx[i];
            if(next_x < 1 || next_x > map_size || next_y < 1 || next_y > map_size) continue;
            if(graph[next_y][next_x] == 0 || visited[next_y][next_x]) continue;

            q.push({next_y, next_x});
            visited[next_y][next_x] = true;
        }
    }
}
int main() {
    cin >> map_size;
    for(int y = 1; y <= map_size; y++) {
        for (int x = 1; x <= map_size; x++) {
            int temp;
            scanf("%1d", &temp);
            graph[y][x] = temp;
        }
    }

    int idx = 0;
    for (int i = 1; i <= map_size; i++) {
        for (int j = 1; j <= map_size; j++) {
            if(graph[i][j] == 1 && !visited[i][j]){
                apartment_count = 0;
                q.push({i, j});
                visited[i][j] = true;
                bfs();
                apartment[idx++] = apartment_count;
            }
        }
    }
    sort(idx);
    cout << idx << endl;
    for (int i = 0; i < idx; i++) {
        cout << apartment[i] << endl;
    }
    return 0;
}
