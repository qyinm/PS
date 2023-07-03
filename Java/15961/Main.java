import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int variation = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int couponNumber = Integer.parseInt(st.nextToken());


        int[] rail = new int[n];
        for (int i = 0; i < n; i++) {
            rail[i] = Integer.parseInt(br.readLine());
        }

        int[] check = new int[variation + 1];
        
        int maxCnt = 0;
        int l = 0;
        int r = 0;
        int cnt = 0;
        for(; r < k; r++) {
            if (check[rail[r%n]]++ == 0)    cnt++;
        }
        maxCnt = cnt;
        if (check[couponNumber] == 0) maxCnt++;
        
        
        while (l < n) {
            if(--check[rail[l]] == 0)   --cnt;
            if (check[rail[r%n]]++ == 0)    cnt++;
            if (check[couponNumber] == 0) {
                maxCnt = Math.max(maxCnt, cnt + 1);
            } else {
                maxCnt = Math.max(maxCnt, cnt);
            }
            l++;
            r++;
        }
        System.out.println(maxCnt);

    }
}
