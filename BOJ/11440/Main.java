import java.util.*;
import java.io.*;

class Main{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    final long MOD = (long)(1e9+7);
    public long[][] mul(long[][] m1, long[][] m2) {
        long[][] ret = new long[2][2];
        for(int i = 0; i < 2; i++) {
            for(int j = 0; j < 2; j++) {
                for(int k = 0; k < 2; k++) {
                    ret[i][j] += m1[i][k] * m2[k][j] % MOD;
                }
            }
        }
        
        return ret;
    }
    
    public long[][] divide(long n, long[][] mx) {
        if (n == 1) {
            return mx;
        }
        if (n % 2 == 1) {
            return mul(mx, divide(n-1, mx));
        } else {
            long[][] half = divide(n / 2, mx);
            return mul(half, half);
        }
    }
    
    public void solve() throws Exception {
        long n = Long.parseLong(br.readLine());
        long[][] mat = {{1, 1}, {1, 0}};
        long[][] ret = divide(n, mat);
        System.out.println(ret[0][0]*ret[0][1]%MOD);
    }
    
    public static void main(String[] args) throws Exception {
        new Main().solve();
    }
}
