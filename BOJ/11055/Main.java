import java.util.*;
import java.io.*;
public class Main
{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    public void solve() throws Exception {
        int n = Integer.parseInt(br.readLine());
        
        int[] dp = new int[n];
        int[] data = new int[n];
        st = new StringTokenizer(br.readLine());
        
        for(int i = 0; i < n; i++) {
            data[i] = Integer.parseInt(st.nextToken());
        }
        
        int ans = -1;
        for (int i = n-1; i >= 0; i--) {
            dp[i] = data[i];
            int add = 0;
            for (int j = i+1; j < n; j++) {
                if (data[i] < data[j]) {
                    add = Math.max(dp[j], add);
                }
            }
            dp[i] += add;
            ans = Math.max(dp[i], ans);
        }
        
        System.out.println(ans);
    }
    
	public static void main(String[] args) throws Exception {
		new Main().solve();
	}
}
