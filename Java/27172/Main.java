import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n;
    static Map<Integer, Integer> numbers;
    public static void main(String[] args) throws Exception {
        n = Integer.parseInt(br.readLine());
        numbers = new LinkedHashMap<Integer, Integer>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        
        while (st.hasMoreTokens()) {
            numbers.put(Integer.parseInt(st.nextToken()), 0);
        }
        
        List<Integer> keyMap = numbers.entrySet().stream()
                                    .map(t -> t.getKey())
                                    .sorted((a, b) -> a.compareTo(b))
                                    .collect(Collectors.toList());
                                    
        int[] chei = new int[1000001];
        keyMap.stream().forEach(key -> chei[key] = 1);
        for (int key: keyMap) {
            for (int w = key + key; w <= keyMap.get(n-1); w += key) {
                if (chei[w] == 1) {
                    numbers.put(w, numbers.get(w) - 1);
                    numbers.put(key, numbers.get(key) + 1);
                }
            }
        }
        numbers.entrySet().forEach(entry -> System.out.print(entry.getValue() + " "));
    }
}
