import java.io.*;
import java.util.*;
import java.util.stream.*;

class Main {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n;
    int[][][] cache;

    public void solve() throws Exception{
        n = Integer.parseInt(br.readLine());
        int mod = 1000000000;
        cache = new int[101][10][1 << 10];
        int ans = 0;
        for (int idx = 1; idx < 10; idx++) {
            cache[1][idx][1 << idx] = 1;
        }
        
        for (int i = 2; i <= n; ++i) {
            for (int j = 0; j <= 9; ++j) {
                for (int k = 0; k <= (1 << 10) - 1; ++k) {
                    if (j == 0)
                        cache[i][0][k | (1 << 0)] = (cache[i][0][k | (1 << 0)] + cache[i - 1][1][k]) % mod;
                    else if (j == 9)
                        cache[i][9][k | (1 << 9)] = (cache[i][9][k | (1 << 9)] + cache[i - 1][8][k]) % mod;
                    else {
                        cache[i][j][k | (1 << j)] = (cache[i][j][k | (1 << j)] + cache[i - 1][j - 1][k]) % mod;
                        cache[i][j][k | (1 << j)] = (cache[i][j][k | (1 << j)] + cache[i - 1][j + 1][k]) % mod;
                    }
                }
            }
        }

        for (int j = 0; j <= 9; ++j)
            ans = (ans + cache[n][j][(1<<10) - 1]) % mod;
        System.out.println(ans);
    }

    public static void main(String[] args) throws Exception {
        new Main().solve();
    }
}