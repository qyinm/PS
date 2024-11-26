#include<iostream>
#include<vector>

using namespace std;

vector<vector<int>> graph;

void dfs(int currentNode, vector<int>& parents) {
    for (const int& node : graph[currentNode]) {
        if (parents[node] != -1) {
            continue;
        }
        parents[node] = currentNode;
        dfs(node, parents);
    }
}

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    
    int nodeCount = 0;
    cin >> nodeCount;
    graph = vector<vector<int>>(nodeCount + 1, vector<int>(0));
    
    int nodeA, nodeB;
    for (int i = 0; i < nodeCount - 1; i++) {
        cin >> nodeA >> nodeB;
        graph[nodeA].push_back(nodeB);
        graph[nodeB].push_back(nodeA);
    }
    vector<int> parents(nodeCount + 1, -1);
    parents[1] = 0;
    dfs(1, parents);
    for (int findNode = 2; findNode <= nodeCount; findNode++) {
        cout << parents[findNode] << "\n";
    }

    return 0;
}