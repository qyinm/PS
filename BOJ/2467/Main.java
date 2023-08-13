import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);

        int lP = arr[0];
        int rP = arr[n-1];
        int minGap = arr[0] + arr[n-1];

        int left = 0;
        int right = n-1;
        while (left < right) {
            int gap = arr[right] + arr[left];
            if (Math.abs(gap) <= Math.abs(minGap)) {
                lP = arr[left];
                rP = arr[right];
                minGap = gap;
            }
            if (gap == 0)   break;
            if (gap > 0)    right--;
            else    left++;
        }

        System.out.println(lP + " " + rP);
    }
}