import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.*;

class Main {

    public BigDecimal expo(BigDecimal a, BigDecimal b) {
        if (b.equals(BigDecimal.ONE)) {
            return a;
        }
        var ret = expo(a, b.divide(BigDecimal.valueOf(2), RoundingMode.DOWN));
        ret = ret.pow(2);
        if (b.remainder(BigDecimal.valueOf(2)).equals(BigDecimal.ONE)){
            ret = ret.multiply(a);
        }
        return ret;
    }

    public void solve() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        BigDecimal a = new BigDecimal(st.nextToken());
        BigDecimal b = new BigDecimal(st.nextToken());
        System.out.println(expo(a, b).toPlainString());
    }

    public static void main(String[] args) throws Exception {
        new Main().solve();
    }
}