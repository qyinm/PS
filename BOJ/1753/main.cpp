#include <iostream>
#include <vector>
#include <queue>

#define inf 999999999
using namespace std;


int v, e;
int start;



void dijkstra(vector<vector<pair<int, int>>> &graph, vector<int> &cost) {
    cost[start] = 0;
    priority_queue<pair<int, int>> pq;
    pq.push({0, start});

    while (!pq.empty()) {
        int current_node = pq.top().second;
        int weight = -pq.top().first;
        pq.pop();

        for (auto &g: graph[current_node]) {
            int next_weight = g.first + weight;
            int next_node = g.second;
            if (cost[next_node] <= next_weight)
                continue;
            cost[next_node] = next_weight;
            pq.push({-next_weight, next_node});
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> v >> e;
    cin >> start;

    vector<vector<pair<int, int>>> graph(v + 1);
    vector<int> cost(v + 1, inf);
    for (int i = 0; i < e; i++) {
        int tu, tv, tw;
        cin >> tu >> tv >> tw;
        graph[tu].push_back({tw, tv});
    }

    dijkstra(graph, cost);

    for (int i = 1; i <= v; i++) {
        if (cost[i] == inf) {
            cout << "INF\n";
        } else {
            cout << cost[i] << "\n";
        }
    }
    return 0;
}