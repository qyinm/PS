import java.util.*;
import java.util.stream.Collectors;
import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        
        int[] list = Arrays.stream(br.readLine().split(" "))
                            .mapToInt(Integer::parseInt)
                            .map(e -> e % 2 == 0 ? 1 : 0).toArray();
        
        int sp = 0;
        int cp = 0;
        int maxL = 0;
        int len = 0;
        while (cp < n) {
            while(k >= 0) {
                k -= (list[cp] == 0 ? 1 : 0);
                len += list[cp];
                cp += 1;
                if (cp == n) {
                    break;
                }
            }
            maxL = Math.max(maxL, len);
            while (k < 0) {
                k += list[sp] == 0 ? 1 : 0;
                len -= list[sp++];
            }
        }

        System.out.println(maxL);
    }
}