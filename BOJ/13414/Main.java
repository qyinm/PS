import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int k = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());

        // 순서를 보장해주는 HashMap
        LinkedHashMap<String, Integer> map = new LinkedHashMap<>();

        for (int i = 0; i < l; i++) {
            String id = br.readLine();
            if (map.containsKey(id))    map.remove(id);
            map.put(id, 1);
        }

        map.entrySet()
            .stream()
            .map(entry -> entry.getKey())
            .limit(k)
            .forEach(System.out::println);
    }
}
