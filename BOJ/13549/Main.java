import java.io.*;
import java.util.*;

public class Main {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    
    int n, k;
    int[] cache;
    
    public boolean valid(int idx) {
        return (0 <= idx && idx <= 100000);
    }
    
    public int acc(int cmd, int num) {
        switch(cmd) {
            case 1:
                num += 1;
                break;
            case 2:
                num *= 2;
                break;
            case 3:
                num -= 1;
                break;
        }
        return num;
    }
    
    public void solve() throws Exception {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        cache = new int[100001];
        Arrays.fill(cache, 987654321);
        cache[n] = 0;
        
        Deque<Integer> queue = new ArrayDeque<>();
        queue.addLast(n);
        while (!queue.isEmpty()) {
            int cur = queue.pollFirst();
            if (cur == k) {
                break;
            }
            for (int i = 1; i <= 3; i++) {
                int next = acc(i, cur);
                if (!valid(next) || cache[next] < cache[cur] + i % 2) {
                    continue;
                }
                cache[next] = cache[cur] + i % 2;
                queue.addLast(next);
            }
        }
        System.out.println(cache[k]);
    }
    
	public static void main(String[] args) throws Exception {
		new Main().solve();
	}
}
