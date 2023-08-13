import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        FastReader fr = new FastReader();
    
        int n = fr.nextInt();
        ArrayDeque<Integer> inSt = new ArrayDeque<>();
        int[] countDb = new int[n];

        for (int i = 0; i < n; i++) {
            int curInt = fr.nextInt();
            inSt.addLast(curInt);
            countDb[curInt] += 1;
        }
        
        ArrayDeque<Integer> ansSt = new ArrayDeque<>();
        while(!inSt.isEmpty()) {
            Integer instTop = inSt.pollLast();
            if (ansSt.isEmpty()) {
                ansSt.addLast(instTop);
                System.out.print("-1 ");
                continue;
            }

            while (ansSt.peekLast() <= instTop) {
                ansSt.pollLast();
            }
        }

        for (int i = 0; i < n; i++) {

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