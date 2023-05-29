import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        FastReader fr = new FastReader();
        
        // input data
        int n = fr.nextInt();
        int[] height = new int[n];
        for (int i = 0; i < n; i++) {
            height[i] = fr.nextInt();
        }
        
        
        Stack<Pair> st = new Stack<>();
        long[] ans = new long[n];
        for (int i = n - 1; i >= 0; i--) {
            while(!st.isEmpty()) {
                if (height[i] > st.peek().height) {
                    ans[i] += ans[st.peek().idx] + 1;
                    st.pop();
                } else {
                    break;
                }
            }

            st.add(new Pair(i, height[i]));
        }

        long ansSum = 0;
        for (int i = 0; i < n; i++) {
            ansSum += ans[i];
        }
        System.out.println(ansSum);
    }
    public static class Pair {
        int idx, height;

        Pair(int idx, int height) {
            this.idx = idx;
            this.height = height;
        }
    }
    public static class FastReader {
        BufferedReader br;
        StringTokenizer st;
        public FastReader() { br = new BufferedReader(new InputStreamReader(System.in)); }
        public FastReader(String s) throws FileNotFoundException { br = new BufferedReader(new FileReader(new File(s))); }
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try { st = new StringTokenizer(br.readLine()); }
                catch (IOException e) { e.printStackTrace(); }
            }
            return st.nextToken();
        }
        int nextInt() { return Integer.parseInt(next()); }
        long nextLong() { return Long.parseLong(next()); }
        double nextDouble() { return Double.parseDouble(next()); }
        String nextLine() {
            String str = "";
            try { str = br.readLine(); }
            catch (IOException e) { e.printStackTrace(); }
            return str;
        }
    }
}