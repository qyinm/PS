#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Edge {
    int to;
    int distance;
};

const int INF = 987654321;

vector<long long> dijkstra(int start, int n, const vector<vector<Edge>>& graph) {
    
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
    vector<long long> distances(n, INF);
    distances[start] = 0;
    pq.push({0, start});

    while (!pq.empty()) {
        auto [current_distance, current_node] = pq.top();
        pq.pop();

        for (const auto& gr : graph[current_node]) {
            long long new_distance = current_distance + gr.distance;
            if (distances[gr.to] > new_distance) {
                distances[gr.to] = new_distance;
                pq.push({new_distance, gr.to});
            }
        }
    }

    return distances;
}

int main() {
    int n, e;

    cin >> n >> e;
    vector<vector<Edge>> graph(n);

    int a, b, dist;

    for (int i = 0; i < e; i++) {
        cin >> a >> b >> dist;
        graph[a - 1].push_back({b - 1, dist});
        graph[b - 1].push_back({a - 1, dist});
    }
    int v1, v2;
    cin >> v1 >> v2;
    v1 -= 1;
    v2 -= 1;
    auto dis0 = dijkstra(0, n, graph);
    auto dis1 = dijkstra(v1, n, graph);
    auto dis2 = dijkstra(v2, n, graph);

    long long ans = min(dis0[v1] + dis1[v2] + dis2[n - 1], dis0[v2] + dis2[v1] + dis1[n - 1]);
    if (ans >= INF) {
        ans = -1;
    }
    cout << ans;

    return 0;
}