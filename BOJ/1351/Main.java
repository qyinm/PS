import java.util.*;
import java.util.stream.IntStream;
import java.util.stream.LongStream;
import java.io.*;

class Main {
    static HashMap<Long, Long> map = new HashMap<>();
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        long n = Long.parseLong(st.nextToken());
        int p = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        
        System.out.println(solve(n, p, q));
    }

    public static long solve(long n, int p, int q) {
        if (n == 0) return 1;
        if (map.containsKey(n)) return map.get(n);
        map.put(n, solve(n/q, p, q) + solve(n/p, p, q));
        return map.get(n);
    }
}