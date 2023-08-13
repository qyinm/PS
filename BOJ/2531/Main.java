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
        
        int distinct = 0;
        int maxCnt = 0;
        int flag;
        for(int i = 0; i < n; i++) {
            check = new int[variation + 1];
            flag = 1;
            distinct = 0;
            for (int j = i; j < i + k; j++) {
                if (check[rail[j%n]] == 1)    distinct++; 
                else    check[rail[j%n]] = 1;

                if (rail[j%n] == couponNumber) flag = 0;
            }
            maxCnt = Math.max(maxCnt, k - distinct + flag);
        }

        System.out.println(maxCnt);
    }
}
