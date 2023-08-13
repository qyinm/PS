import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

class Main {
    static int[] visited;
    static int n;
    static int m;
    static int[] result;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        result = new int[m];
        visited = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            result[0] = i;
            solve(i, 1);
        }
    }

    public static void solve(int k, int len) {
        if (len == m) {
            Arrays.stream(result).forEach(t -> System.out.print(t + " "));
            System.out.println();
            return;
        }
        
        for (int i = k + 1; i <= n; i++) {
            if (visited[i] == 1)    continue;
            result[len] = i;
            visited[i] = 1;
            solve(i, len + 1);
            visited[i] = 0;
        }
    }
}