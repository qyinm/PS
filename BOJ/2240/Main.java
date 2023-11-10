import java.io.*;
import java.util.*;
class Main {
    
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    int[] jadu;
    int[][][] cache;
    int t, w;
    public void solve() throws Exception {
        st = new StringTokenizer(br.readLine());
        t = Integer.parseInt(st.nextToken());
        w = Integer.parseInt(st.nextToken());
        
        jadu = new int[t];
        
        for (int i = 0; i < t; i++) {
            jadu[i] = Integer.parseInt(br.readLine());
        }
        

        cache = new int[2][w+1][t];
        for (int[][] cach: cache) {
            for (int[] cac: cach) {
                Arrays.fill(cac, -1);
            }
        }
        
        int ans = Math.max(dp(0, 0, 0), dp(1, 1, 0));
        System.out.println(ans);
    }
    
    public int dp(int move, int position, int idx) {
        if (idx == t) {
            return 0;
        }
        
        if (cache[position][move][idx] != -1) {
            return cache[position][move][idx];
        }
        
        int add = position + 1 == jadu[idx] ? 1 : 0;
        
        
        if (move == w) {
            cache[position][move][idx] = dp(move, position, idx+1) + add;
        } else {
            cache[position][move][idx] = Math.max(dp(move + 1, ~position + 2, idx+1), dp(move, position, idx+1)) + add;
        }

        return cache[position][move][idx];
    }
    
    public static void main(String[] args) throws Exception {
        new Main().solve();
    }
}
