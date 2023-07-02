import java.util.*;
import java.util.stream.IntStream;
import java.util.stream.LongStream;
import java.io.*;

class Main {
    static long[] dp;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        long n = Long.parseLong(st.nextToken());
        int p = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        dp = new long[500001];
        dp[0] = 1;
        IntStream.rangeClosed(1, 500000).
                    forEach(k -> dp[k] = dp[k/q] + dp[k/p]);
        System.out.println(solve(n, p, q));
    }

    public static long solve(long n, int p, int q) {
        if (n > 500000) {
            return solve(n/p, p, q) + solve(n/q, p, q);
        }
        return dp[(int)n];
    }
}