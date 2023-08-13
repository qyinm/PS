import java.io.*;
import java.util.*;
import java.util.stream.*;

class Main {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n;
    int[][][] cache;

    public int dp(int idx, int num, int bit) {

        if (cache[bit][idx][num] != 0) {
            return cache[bit][idx][num];
        }
        if (idx == n)   return bit == (1 << 10) - 1 ? 1 : 0;
        int res = 0;
        if (num + 1 < 10)
            res += dp(idx + 1, num + 1, bit | 1 << (num + 1));
        if (num - 1 >= 0)
            res += dp(idx + 1, num - 1, bit | 1 << (num -1));
        return cache[bit][idx][num] = res % 1000000000;
    }

    public void solve() throws Exception{
        n = Integer.parseInt(br.readLine());

        cache = new int[1 << 11][101][10];
        
        long sum= 0;
        for (int i = 1; i < 10; i++) {
            sum += dp(1, i, 1 << i);
            sum %= 1000000000;
        }

        System.out.println(sum);
    }

    public static void main(String[] args) throws Exception {
        new Main().solve();
    }
}