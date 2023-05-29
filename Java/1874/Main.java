import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        FastReader fr = new FastReader();

        int n = fr.nextInt();
        ArrayList<String> seq = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            seq.add(fr.nextLine());
        }
        ArrayDeque<Integer> dq = new ArrayDeque<>();

        int idx = 0;
        ArrayList<String> ans = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            dq.addLast(i);
            ans.add("+");

            while (!dq.isEmpty() && dq.peekLast() == Integer.parseInt(seq.get(idx))) {
                dq.pollLast();
                ans.add("-");
                idx++;
            }
        }

        if (!dq.isEmpty()) {
            System.out.println("NO");
        } else {
            for (int i = 0; i < ans.size(); i++) {
                System.out.println(ans.get(i));
            }
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
