import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * Main
 */

public class Main {
    public static void main(String[] args) {
        FastReader fr = new FastReader();
        ArrayList<Character> charList = new ArrayList<>();

        char[] str = fr.nextLine().toCharArray();
    
        String bomb = fr.nextLine();
        

        for (int i = 0; i < str.length; i++) {
            charList.add(str[i]);
            if (charList.size() < bomb.length())  continue;
            if (bomb.charAt(bomb.length() - 1) != str[i])   continue;
            int flag = 1;
            for (int j = 0; j < bomb.length(); j++) {
                if (charList.get(charList.size() - bomb.length() + j) != bomb.charAt(j)) {
                    flag = 0;
                    break;
                }
            }
            if (flag == 0) continue;
            for (int j = 0; j < bomb.length(); j++) {
                charList.remove(charList.size() - 1);
            }
        }

        StringBuilder sb = new StringBuilder();
        for (char ch : charList) {
            sb.append(ch);
        }

        String result = sb.toString();
        System.out.println(result.isEmpty() ? "FRULA" : result);
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