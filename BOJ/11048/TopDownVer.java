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

		System.out.println(dp(0, 0));
	}

	public int dp(int y, int x) {
		if (y == n-1 && x == m-1)	return arr[y][x];
		
		
		if (cache[y][x] != -1) {
			return cache[y][x];
		}
        for (int i = 0; i < 3; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];
            if (isNotValid(ny, nx))    continue;
            cache[y][x] = Math.max(cache[y][x], dp(ny, nx) + arr[y][x]);
        }
		
		return cache[y][x];
	}
    
    public boolean isNotValid(int y, int x) {
        return (y >= n || y < 0 || x >= m || x < 0);
    }

	public static void main(String[] args) throws Exception {
		new Main().solve();
	}
}
