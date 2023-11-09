import java.io.*;
import java.util.*;
import java.util.regex.Pattern;
class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static String rex;
    
    public static void main(String[] args) throws Exception {
        int n = Integer.parseInt(br.readLine());
        rex = "^" + br.readLine().replaceAll("\\*", ".*") + "$";
        
        while (n > 0) {
            String s = br.readLine();
            if (Pattern.matches(rex, s)) {
                System.out.println("DA");
            } else {
                System.out.println("NE");
            }
            
            
            n--;
        }
    }
}
