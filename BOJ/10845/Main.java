import java.io.*;
import java.util.*;
import java.util.regex.Pattern;
class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    public void solve() throws Exception {
        Deque<Integer> q = new LinkedList<>();
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            
            String command = st.nextToken();
            
            
                if(command.equals("push")){
                    q.add(Integer.parseInt(st.nextToken()));
                }
                if(command.equals("pop")){
                    Integer pop = q.poll();
                    if (pop == null) {
                        sb.append(-1);
                    } else {
                        sb.append(pop);
                    }
                    sb.append("\n");
                }
                if(command.equals("size")){
                    sb.append(q.size());
                    sb.append("\n");
                }
                if(command.equals("empty")) {
                    
                    if (q.isEmpty()) {
                        sb.append(1);
                    } else {
                        sb.append(0);
                    }
                    sb.append("\n");
                }
                if(command.equals("front")) {
                    Integer peek = q.peek();
                    if (peek == null) {
                        sb.append(-1);
                    } else {
                        sb.append(peek);
                    }
                    sb.append("\n");
                }
                if(command.equals("back")) {
                    Integer peekLast = q.peekLast();
                    if (peekLast == null) {
                        sb.append(-1);
                    } else {
                        sb.append(peekLast);
                    }
                    sb.append("\n");
                }
        }
        System.out.println(sb.toString());
    }
    
    
    
    public static void main(String[] args) throws Exception {
        new Main().solve();
    }
}
