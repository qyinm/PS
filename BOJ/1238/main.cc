#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Edge {
    int to;
    int distance;
};

vector<int> dijkstra(int start, int n, vector<vector<Edge>>& graph) {
    vector<int> distance(n + 1, 1e9);
    distance[start] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
    pq.push({0, start});

    while (!pq.empty()) {
        auto [current_distance, current_node] = pq.top();
        pq.pop();

        for (const auto& edges: graph[current_node]) {
            if (distance[edges.to] > current_distance + edges.distance) {
                distance[edges.to] = current_distance + edges.distance;
                pq.push({distance[edges.to], edges.to});
            }
        }
    }

    return distance;
}

int main() {
    cin.tie(0);
    std::ios_base::sync_with_stdio(0);

    int n, e, x;
    cin >> n >> e >> x;
    vector<vector<Edge>> graph(n + 1);

    for (int i = 0; i < e; i++) {
        int start, end, weight;
        cin >> start >> end >> weight;

        graph[start].push_back({end, weight});
    }

    vector<int> total_distance(n + 1);
    for (int start = 1; start < n + 1; start++) {
        total_distance[start] += dijkstra(start, n, graph)[x];
    }

    vector<int> x_distances = dijkstra(x, n, graph);
    for (int start = 1; start < n + 1; start++) {
        total_distance[start] += x_distances[start];
    }

    int answer = -1;
    for (const auto& dist : total_distance) {
        answer = max(answer, dist);
    }
    cout << answer;
}