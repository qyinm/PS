import java.io.*;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

class Main {
    static int n;
    static int m;
    static int[] result;
    static Integer[] data;
    static int[] visited;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        result = new int[m];

        data = new Integer[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            data[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(data);
        visited = new int[data[n-1] + 1];

        for (int i = 0; i < n; i++) {
            result[0] = data[i];
            visited[data[i]] = 1;
            solve(i, 1);
            visited[data[i]] = 0;
        }
    }

    public static void solve(int k, int len) {
        if (len == m) {
            Arrays.stream(result).forEach(t -> System.out.print(t + " "));
            System.out.println();
            return;
        }
        
        for (int i = 0; i < n; i++) {
            if (data[i] == data[k]) continue;
            if (visited[data[i]] == 1) continue;
            visited[data[i]] = 1;
            result[len] = data[i];
            solve(i, len + 1);
            visited[data[i]] = 0;
        }
    }
}