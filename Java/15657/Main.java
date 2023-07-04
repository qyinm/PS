import java.io.*;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

class Main {
    static int n;
    static int m;
    static int[] result;
    static Integer[] data;
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

        for (int i = 0; i < n; i++) {
            result[0] = data[i];

            solve(i, 1);
        }
    }

    public static void solve(int k, int len) {
        if (len == m) {
            Arrays.stream(result).forEach(t -> System.out.print(t + " "));
            System.out.println();
            return;
        }
        
        for (int i = k; i < n; i++) {
            result[len] = data[i];
            solve(i, len + 1);
        }
    }
}