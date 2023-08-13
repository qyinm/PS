import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        FastReader fr = new FastReader();
        int n = fr.nextInt();
        ArrayDeque<Pair> dq = new ArrayDeque<>();

        long ans = 0;
        
        for (int i = 0; i < n; i++) {
            long person = 1;
            long inHeight = fr.nextLong();
            
            while(!dq.isEmpty() && dq.peekLast().height <= inHeight) {
                ans += dq.peekLast().person;
                if (dq.peekLast().height == inHeight) {
                    person += dq.peekLast().person;
                }
                dq.pollLast();
            }

            if (!dq.isEmpty()) {
                ans += 1;
            }
            

            dq.addLast(new Pair(inHeight, person));
        }
        System.out.println(ans);
    }
    public static class Pair {
        long height, person;

        Pair(long height, long person) {
            this.height = height;
            this.person = person;
        }
    }
    public static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        public FastReader(String s) throws FileNotFoundException {
            br = new BufferedReader(new FileReader(new File(s)));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}