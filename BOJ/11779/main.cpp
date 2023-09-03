#include <iostream>
#include <vector>
#include <queue>


using namespace std;

const int INF = 2000000000;
int v, e;
int start, en;

int before[1001];
int cost[1001];
void dijkstra(vector<vector<pair<int, int>>> &graph) {
    cost[start] = 0;
    priority_queue<pair<int, int>> pq;
    pq.push({0, start});

    while (!pq.empty()) {
        int current_node = pq.top().second;
        int weight = -pq.top().first;
        pq.pop();

        if (cost[current_node] < weight)    continue;

        for (auto &g: graph[current_node]) {
            int next_weight = g.first;
            int next_node = g.second;
            if (cost[next_node] <= weight + next_weight) {
                continue;
            }
            cost[next_node] = next_weight + weight;
            
            before[next_node] = current_node;
            pq.push({-cost[next_node], next_node});
        }
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> v >> e;
   
   
    vector<vector<pair<int, int>>> graph(v + 1);
    
    for (int i = 1; i <= v; i++) {
        cost[i] = INF;
    }

    for (int i = 0; i < e; i++) {
        int tu, tv, tw;
        cin >> tu >> tv >> tw;
        graph[tu].push_back({tw, tv});
    }
    cin >> start >> en;
    dijkstra(graph);

    vector<int> print;
    int temp = en;
    while (temp) {
        print.push_back(temp);
        temp = before[temp];
    }

    cout << cost[en] << '\n';
    cout << print.size() << '\n';
    for (int i = print.size()-1; i >= 0; i--) {
        cout << print[i] << ' ';
    }
    
    return 0;
}