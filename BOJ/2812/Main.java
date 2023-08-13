import java.util.*;
import java.util.stream.Collectors;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<Integer> stack = new Stack<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        List<Integer> list = Arrays.stream(br.readLine().split("")).map(Integer::parseInt).collect(Collectors.toList());
        stack.add(list.get(0));
        for (int i = 1; i < n; i++) {
            
            while(k != 0 && !stack.isEmpty() && stack.peek() < list.get(i)) {
                stack.pop();
                k--;
            }
            stack.add(list.get(i));            
        }
        while (k != 0) {
            stack.pop();
            k--;
        }
        if (stack.isEmpty()) {
            stack.add(0);
        }
        String ans = stack.stream().map(t->t.toString()).collect(Collectors.joining(""));
        System.out.println(ans);
    }
}
