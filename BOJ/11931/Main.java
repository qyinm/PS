import java.util.Collections;
import java.util.*;
import java.io.*;

public class Main
{
	public static void main(String[] args) throws Exception {
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(br.readLine());
		
		Integer[] arr = new Integer[n];
		for (int i = 0; i < n; i++) {
		    arr[i] = Integer.parseInt(br.readLine());
		}
		
		Arrays.sort(arr, Collections.reverseOrder());
		
	    for (int i = 0; i < n; i++) {
	        sb.append(arr[i]).append("\n");
	    }
	    
	    System.out.println(sb.toString());
	}
}
