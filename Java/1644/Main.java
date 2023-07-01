import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] sieve = new int[4000001];
        int[] prime = new int[4000001];
        int primeIdx = 0;
        for (int i = 2; i <= n; i++) {
            if (sieve[i] == 1)  continue;
            prime[primeIdx++] = i;
            for (int j = i + i; j <= n; j += i) sieve[j] = 1;
        }

        
        int cnt = 0;
        for (int i = 0; i < primeIdx; i++) {
            int sum = 0;
            for (int j = i; j < primeIdx; j++) {
                    
                sum += prime[j];
                if (sum > n) break;
                if (sum == n) {
                    cnt++;
                    break;
                }
            }
        }
        System.out.println(cnt);
    }
}