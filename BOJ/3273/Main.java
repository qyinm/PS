import java.util.*;
import java.io.*;
public class Main
{
    
	public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		boolean[] arr = new boolean[2000001];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		List<Integer> nums = new ArrayList<>();
		for (int i = 0; i < n; i++) {
		    int in = Integer.parseInt(st.nextToken());
		    arr[in] = true;
		    nums.add(in);
		}
		
		int k = Integer.parseInt(br.readLine());
		
		long ans = nums.stream().filter(e -> (k-e > 0) && arr[k-e])
		                .count();
		
		System.out.println(ans / 2);
	}
}
