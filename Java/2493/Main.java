import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

/**
 * Main
 */
public class Main {
    static int n;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        n = Integer.parseInt(br.readLine());
        Stack<Pair> stack = new Stack<>();
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int height = Integer.parseInt(st.nextToken());
            
            while (!stack.empty()) {
                if (height < stack.peek().height) {
                    break;
                }
                stack.pop();
            }
            
            if (stack.empty()) {
                System.out.print("0 ");
            } else {
                System.out.print(stack.peek().idx + 1 +" ");
            }
            stack.push(new Pair(height, i));
        }
    }

    public static class Pair {
        int height, idx;
        Pair (int height, int idx) {
            this.height = height;
            this.idx = idx;
        }
    }
}