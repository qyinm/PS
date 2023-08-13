import java.util.*;
import java.util.stream.IntStream;
import java.io.*;

class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = null;
    static int n;
    static int m;
    static int k;
    static int[] candy;
    static int[][] friendship;

    public static void main(String[] args) throws Exception {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        candy = new int[n + 1];
        IntStream.rangeClosed(1, n)
                .forEach(t -> candy[t] = Integer.parseInt(st.nextToken()));
        
        friendship = new int[n + 1][n + 1];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            friendship[a][b] = 1;
        }
    }

    public static void dfs(int idx, int cnt)
}