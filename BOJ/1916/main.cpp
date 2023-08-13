#include <iostream>
#include <vector>
#include <queue>

#define inf 0x3f3f3f3f
using namespace std;



int size;

int dijkstra(int start, int end, const vector<vector<pair<int, int>>> &graph) {
    priority_queue<pair<int, int>> pq;
    vector<int> cost(size + 1, inf);

    cost[start] = 0;
    pq.push({0, start});

    while (!pq.empty()) {
        int weight = -pq.top().first;
        int current = pq.top().second;
        pq.pop();
        if (cost[current] < weight) continue;
        for (const auto &g: graph[current]) {
            int next_node = g.second;
            int next_cost = g.first + weight;
            if (cost[next_node] <= next_cost) continue;
            cost[next_node] = next_cost;
            pq.push({-next_cost, next_node});
        }
    }

    return cost[end];
}

void input(vector<vector<pair<int, int>>> &graph, int edge) {
    for (int e = 0; e < edge; e++) {
        int src, dest, weight;
        cin >> src >> dest >> weight;
        graph[src].push_back({weight, dest});
    }
}

int main() {
    int edge;

    cin >> size;
    cin >> edge;

    vector<vector<pair<int, int>>> graph(size + 1);
    input(graph, edge);

    int start, end;
    cin >> start >> end;

    int ans = dijkstra(start, end, graph);

    cout << ans;
    return 0;
}
