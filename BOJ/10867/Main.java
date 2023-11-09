import java.util.Collections;
import java.util.*;
import java.io.*;

public class Main
{
	public static void main(String[] args) throws Exception {
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(br.readLine());
		
		TreeSet<Integer> tr = new TreeSet<>();
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
		    tr.add(Integer.parseInt(st.nextToken()));
		}
		
	    for (Integer i : tr) {
	        sb.append(i).append(" ");
	    }
	    
	    System.out.print(sb.toString());
	}
}
