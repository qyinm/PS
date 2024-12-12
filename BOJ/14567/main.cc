#include <iostream>
#include <vector>
#include <stack>

using namespace std;

void top_sort(int current_course, const vector<vector<int>>& graph, vector<int>& semester) {
    for (const auto& next_course : graph[current_course]) {
        semester[next_course] = max(semester[next_course], semester[current_course] + 1);
    }
}

int main() {
    cin.tie(0);
    std::ios_base::sync_with_stdio(0);
    
    int n, e;
    cin >> n >> e;

    vector<int> semester(n + 1, 1);
    vector<vector<int>> graph(n + 1);
    for (int i = 0; i < e; i++) {
        int precourse, course;
        cin >> precourse >> course;
        graph[precourse].push_back(course);
    }

    for (int i = 1; i < n + 1; i++) {
        top_sort(i, graph, semester);
    }

    for (int i = 1; i < n + 1; i++) {
        cout << semester[i] << " ";
    }
}