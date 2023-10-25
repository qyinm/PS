import java.util.*;
import java.io.*;
public class Main
{
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	StringTokenizer st;
	int n, m;
	int[][] arr;
	int[][] cache;
	int[] dx = {1, 1, 0};
	int[] dy = {0, 1, 1};
	public void solve() throws Exception {

		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());

		arr = new int[n][m];
		cache = new int[n][m];

		for (int[] c: cache) Arrays.fill(c, -1);
		
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		cache[0][0] = arr[0][0];
		
		Queue<int[]> q = new LinkedList<>();
		q.add(new int[]{0, 0});
		while(!q.isEmpty()) {
		    int[] peek = q.poll();
		    int x = peek[1];
		    int y = peek[0];
		    for (int i = 0; i < 3; i++) {
		        int nx = x + dx[i];
		        int ny = y + dy[i];
		        
		        if (isValid(ny, nx))   continue;
		        if (cache[y][x] + arr[ny][nx] > cache[ny][nx]) {
		            cache[ny][nx] = cache[y][x] + arr[ny][nx];
		            q.add(new int[]{ny, nx});
		        }
		    }
		}
		
		System.out.println(cache[n-1][m-1]);
	}
	
	public boolean isValid(int y, int x) {
	    return (y < 0 || y >= n || x < 0 || x >= m);
	}


	public static void main(String[] args) throws Exception {
		new Main().solve();
	}
}
