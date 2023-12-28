import java.util.*;
import java.io.*;

public class Main {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    
    boolean[][][] visited;
    int[][] graph;
    
    int n, m, k;
    
    int[] dr = {0, 1, 0, -1};
    int[] dc = {1, 0, -1, 0};
    
    public boolean isValid(int cur_row, int cur_col) {
        if (cur_row < 0 || cur_row >= n || cur_col < 0 || cur_col >= m) {
            return false;
        }
        return true;
    }
    
    public int bfs() {
        Deque<int[]> queue = new  ArrayDeque<>();
        queue.addLast(new int[]{0, 0, k, 1, 1});
        visited[k][0][0] = true;
        
        while (!queue.isEmpty()) {
            int[] cur = queue.pollFirst();
            if (cur[0] == n-1 && cur[1] == m-1) {
                return cur[3];
            }
            for (int i = 0; i < 4; i++) {
                int nr = cur[0] + dr[i];
                int nc = cur[1] + dc[i];
                
                if (!isValid(nr, nc)) {
                    continue;
                }
                
                if (graph[nr][nc] == 0) {
                    if (visited[cur[2]][nr][nc]) {
                        continue;
                    }
                    visited[cur[2]][nr][nc] = true;
                    queue.addLast(new int[]{nr, nc, cur[2], cur[3] + 1, -cur[4]});
                }
                else if (graph[nr][nc] == 1 && cur[2] == 0) {
                    continue;
                }
                else if (graph[nr][nc] == 1 && cur[4] == -1) {
                    queue.addLast(new int[]{cur[0], cur[1], cur[2], cur[3] + 1, 1});
                }
                else if (graph[nr][nc] == 1) {
                    if (visited[cur[2]-1][nr][nc]) {
                        continue;
                    }
                    visited[cur[2]-1][nr][nc] = true;
                    queue.addLast(new int[]{nr, nc, cur[2] - 1, cur[3] + 1, -1});
                }
            }
        }
        return -1;
    }
    
    public void solve() throws Exception {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        
        graph = new int[n][m];
        visited = new boolean[k+1][n][m];
        
        for (int i = 0; i < n; i++) {
            String a = br.readLine();
            for (int j = 0; j < m; j++) {
                graph[i][j] = a.charAt(j) - '0';
            }
        }
        int answer = bfs();
        System.out.println(answer);
    }
    
	public static void main(String[] args) throws Exception {
		new Main().solve();
	}
}
