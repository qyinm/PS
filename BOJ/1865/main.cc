#include <iostream>
#include <vector>

#define ll long long

using namespace std;

struct Edge
{
    ll to;
    ll distance;
};


bool bellman_ford(vector<vector<Edge>> roads, vector<vector<Edge>> worm_holes, int start, int n) {
    vector<ll> travel_times(n + 1, 1e9);
    travel_times[start] = 0;

    for (int k = 1; k < n; k++) {
        for (int u = 1; u < n + 1; u++) {
            for (const auto& edge: roads[u]) {
                travel_times[edge.to] = min(travel_times[edge.to], travel_times[u] + edge.distance);
            }
            for (const auto& edge: worm_holes[u]) {
                travel_times[edge.to] = min(travel_times[edge.to], travel_times[u] + edge.distance);
            }
        }
    }

    vector<ll> temp = travel_times;

    for (int u = 1; u < n + 1; u++) {
        for (const auto& edge: roads[u]) {
            travel_times[edge.to] = min(travel_times[edge.to], travel_times[u] + edge.distance);
        }
        for (const auto& edge: worm_holes[u]) {
            travel_times[edge.to] = min(travel_times[edge.to], travel_times[u] + edge.distance);
        }
    }

    for (int i = 1; i < n + 1; i++) {
        if (travel_times[i] != temp[i]) {
            return true;
        }
    }

    return false;
}

int main() {
    cin.tie(nullptr);
    std::ios_base::sync_with_stdio(false);

    ll tc, n, m, w, s, e, t;
    cin >> tc;
    while (tc--) {
        cin >> n >> m >> w;
        vector<vector<Edge>> worm_holes(n + 1);
        vector<vector<Edge>> roads(n + 1);
        for (int i = 0; i < m; i++) {
            cin >> s >> e >> t;
            roads[s].push_back({e, t});
            roads[e].push_back({s, t});
        }
        for (int i = 0; i < w; i++) {
            cin >> s >> e >> t;
            worm_holes[s].push_back({e, -t});
        }

        if (bellman_ford(roads, worm_holes, 0, n)) {
            cout << "YES\n";
            continue;
        }
        cout << "NO\n";
    }

    return 0;
}