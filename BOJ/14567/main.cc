#include <iostream>
#include <vector>
#include <stack>

using namespace std;

void top_sort(int current_course, const vector<vector<int>>& graph, stack<int>& st, vector<bool>& visited) {
    visited[current_course] = true;
    for (const auto& next_course : graph[current_course]) {
        if (visited[next_course])   continue;
        top_sort(next_course, graph, st, visited);
    }
    st.push(current_course);
}

int main() {
    cin.tie(0);
    std::ios_base::sync_with_stdio(0);
    
    int n, e;
    cin >> n >> e;

    stack<int> st;
    vector<bool> visited(n + 1);
    vector<vector<int>> graph(n + 1);
    for (int i = 0; i < e; i++) {
        int precourse, course;
        cin >> precourse >> course;
        graph[precourse].push_back(course);
    }

    for (int i = 1; i < n + 1; i++) {
        if (visited[i]) continue;
        top_sort(i, graph, st, visited);
    }

    vector<int> semesters(n + 1, 1);
    while (!st.empty()) {
        int current_course = st.top();
        st.pop();
        
        for (const auto& next_course : graph[current_course]) {
            semesters[next_course] = max(semesters[next_course], semesters[current_course] + 1);
        }
    }

    for (int course = 1; course < n + 1; course++) {
        cout << semesters[course] << " ";
    }
}