import java.util.*;
import java.io.*;

public class Main {
    static char[] str;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            str = br.readLine().toCharArray();
            int left = 0;
            int right = str.length - 1;
            System.out.println(sol(left, right, 0));
        }
    }

    public static int sol(int left, int right, int cnt) {
        int l = left;
        int r = right;
        while(l < r) {
            if (str[l] == str[r]) {
                l++;
                r--;
                continue;
            }

            if (cnt == 1) {
                return 2;
            }

            return Math.min(sol(l+1, r, 1), sol(l, r-1, 1));
        }
        return cnt;
    }
}
