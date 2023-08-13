import java.util.*;
import java.util.stream.IntStream;
import java.io.*;

class Main {
    static int n;
    static int s;
    static int[] data;
    static HashMap<Long, Long> left = new HashMap<>();
    static HashMap<Long, Long> right = new HashMap<>();
    static StringTokenizer st;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        s = Integer.parseInt(st.nextToken());
        data = new int[n];

        st = new StringTokenizer(br.readLine());
        IntStream.range(0, n).forEach(k -> data[k] = Integer.parseInt(st.nextToken()));

        Arrays.sort(data);

        divide(0, n/2, 0, left);
        divide(n/2, n, 0, right);

        long ans = 0;
        for (Map.Entry<Long, Long> entry : left.entrySet()) {
            if(right.get(s - entry.getKey()) != null) {
                ans += entry.getValue() * right.get(s - entry.getKey());
            } else if (entry.getKey() == s) {
                ans += entry.getValue();
            }
        }
        if (ans != 0 && s == 0) ans--;
        System.out.println(ans);
    }

    public static void divide(int start, int end, long sum, HashMap<Long, Long> map) {
        if (start >= end) {
            if (map.containsKey(sum))   map.put(sum, map.get(sum) + 1);
            else    map.put(sum, (long) 1);
            return;
        }
        divide(start+1, end, sum+data[start], map);
        divide(start+1, end, sum, map);
    }


}