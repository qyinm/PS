import java.util.*;
import java.util.stream.*;
import java.io.*;
public class Main
{
    int[] graph = new int[101];
    int[] dist = new int[101];
    
    StringTokenizer st;
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public void solve() throws Exception {
        Arrays.fill(dist, -1);
        IntStream.rangeClosed(1, 100).forEach(el -> graph[el] = el);
        
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        
        for (int i = 0; i < n+m; i++) {
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            
            graph[from] = to;
        }
        
        Queue<Integer> q = new LinkedList<>();
        dist[1] = 0;
        q.add(1);
        
        while(!q.isEmpty()) {
            int curr = q.poll();
            for (int i = 1; i <= 6; i++) {
                int next = curr + i;
                if (next > 100) break;
                next = graph[next];
                if (dist[next] == -1) {
                    dist[next] = dist[curr] + 1;
                    q.add(next);
                }
            }
        }
        System.out.println(dist[100]);
    }
	public static void main(String[] args) throws Exception {
		new Main().solve();
	}
}
