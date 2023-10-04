import java.util.ArrayList;
import java.util.List;
import java.io.*;

class Main {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int[] graph;
    boolean[] visited;
    List<Integer> ans;

    public void solve() throws Exception {
        int n = Integer.parseInt(br.readLine());

        graph = new int[n+1];
        for (int i = 1; i <= n; i++) {
            graph[i] = Integer.parseInt(br.readLine());
        }

        ans = new ArrayList<>();
        visited = new boolean[n+1];
        for (int i = 1; i <= n; i++) {
            visited[i] = true;
            dfs(i, i);
            visited[i] = false;
        }

        System.out.println(ans.size());
        for (Integer el : ans) {
            System.out.println(el);
        }
    }

    public void dfs(int start, int target) {
        if (!visited[graph[start]]) {
            visited[graph[start]] = true;
            dfs(graph[start], target);
            visited[graph[start]] = false;
        }
        if (graph[start] == target) ans.add(target);
    }

    public static void main(String[] args) throws Exception {
        new Main().solve();
    }
}