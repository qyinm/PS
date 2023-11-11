import java.util.*;
import java.io.*;

class Main {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    public void solve() throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        
        Map<String, Integer> person = new TreeMap<>();
        for (int i = 0; i < n; i++) {
            String a = br.readLine();
            person.put(a, 0);
        }
        int cnt = 0;
        for (int i = 0; i < m; i++) {
            String a = br.readLine();
            if (person.containsKey(a)) {
                person.put(a, 1);
                cnt += 1;
            }
        }
        System.out.println(cnt);
        person.entrySet().stream().filter(el -> el.getValue() == 1)
                .map(Map.Entry::getKey)
                .forEach(System.out::println);
    }
    
    public static void main(String[] args) throws Exception {
        new Main().solve();
    }
}
