import java.util.*;
import java.util.stream.*;
import java.io.*;

public class Main
{
    int[] dx = {1, 1, 2, 2, -1, -1, -2, -2};
    int[] dy = {2, -2, 1, -1, 2, -2, 1, -1};
    
    StringTokenizer st;
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    public void solve() throws Exception {
        int tc = Integer.parseInt(br.readLine());
        for (int i = 0; i < tc; i++) {
            int l = Integer.parseInt(br.readLine());
            
            st = new StringTokenizer(br.readLine());
            int[] start = {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
            
            st = new StringTokenizer(br.readLine());
            int[] end = {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
            
            night(start, end, l);
        }
    }
    
    public void night(int[] start, int[] end, int l) {
        int[][] graph = new int[l][l];
        for (int[] g : graph)   Arrays.fill(g, -1);
        
        Queue<int[]> q = new LinkedList<>();
        graph[start[1]][start[0]] = 0;
        q.add(start);
        
        while(!q.isEmpty()) {
            int[] curr = q.poll();
            if (curr[1] == end[1] && curr[0] == end[0]) break;
            for (int i = 0; i < 8; i++) {
                int[] next = {curr[0] + dx[i], curr[1] + dy[i]};
                if (next[0] < 0 || next[0] >= l || next[1] < 0 || next[1] >= l) {
                    continue;
                }
                if (graph[next[1]][next[0]] == -1) {
                    graph[next[1]][next[0]] = graph[curr[1]][curr[0]] + 1;
                    q.add(next);
                }
            }
        }
        System.out.println(graph[end[1]][end[0]]);
    }
    
	public static void main(String[] args) throws Exception {
		new Main().solve();
	}
}
