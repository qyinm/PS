import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class Main {
    static int n = 0;
    static long[][] cache = new long[100][100];
    static int[][] map;
    public static long solve(int x, int y) {
        if (x < 0 || x >= n || y < 0 || y >= n) return 0;
        if (x == n-1 && y == n-1)   return 1;
        if (cache[y][x] == -1) {
            cache[y][x] = 0;
            cache[y][x] = solve(x + map[y][x], y) + solve(x, y + map[y][x]);
        }
        return cache[y][x];
    }

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        map = new int[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(cache[i], -1);
        }
        StringTokenizer st = null;
        for (int i = 0; i < n; i++) { 
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        long ans = solve(0, 0);
        System.out.println(ans);
    }
}