import java.util.*;
import java.io.*;

class Main {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    int n;
    int[] sizedb;
    long[][] dp;


    public void solution() throws IOException{
        n = Integer.parseInt(br.readLine());
        sizedb = new int[n+2];
        dp = new long[n+1][n+1];

        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            sizedb[i] = Integer.parseInt(st.nextToken());
            if (i == n) {
                sizedb[n+1] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; i+j <= n; j++) {
                int y = j+i;
                dp[j][y] = 2147483647;
                for (int k = j; k < y; k++) {
                    dp[j][y] = Math.min(dp[j][y], dp[j][k] + dp[k+1][y] + sizedb[j]*sizedb[k+1]*sizedb[y+1]);
                }
            }
        }
        
        System.out.println(dp[1][n]);
    }

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}