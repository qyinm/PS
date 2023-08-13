import java.io.*;
import java.util.*;

class Main {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    StringBuilder sb = new StringBuilder();
    final long MOD = (long) (1e9 + 7);
    long[] facto = new long[4000001];

    public long divPower(int idx, long p) {
        if (p <= 0) {
            return 1;
        }
        if (p % 2 == 0) {
            long half = divPower(idx, p / 2);
            return half * half % MOD;
        } else {
            return (facto[idx] * divPower(idx, p-1)) % MOD;
        }
    }

    public void bino(int n, int k) {
        long div1 = divPower(n-k, MOD-2) % MOD;
        long div2 = divPower(k, MOD-2) % MOD;
        long div = (div1 * div2) % MOD;
        sb.append(facto[n] * div % MOD).append("\n");
    }

    public void solve() throws Exception {
        int tc = Integer.parseInt(br.readLine());
        
        facto[0] = 1;
        for (int i = 1; i < 4000001; i++) {
            facto[i] = (facto[i-1] * i) % MOD;
        }

        // for (int i = 0; i <= 7; i++) {
        //     System.out.println(facto[i]);
        // }

        for (int i = 0; i < tc; i++) {
            st = new StringTokenizer(br.readLine());
            int n, k;
            n = Integer.parseInt(st.nextToken());
            k = Integer.parseInt(st.nextToken());
            bino(n, k);
        }

        System.out.println(sb.toString());
    }

    public static void main(String[] args) throws Exception {
        new Main().solve();
    }
}