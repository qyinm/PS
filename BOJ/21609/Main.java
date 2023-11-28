import java.util.*;
import java.io.*;

public class Main
{
    int[][] matrix;
    int[] dr = {-1, 0, 1, 0};
    int[] dc = {0, 1, 0, -1};
    PriorityQueue<Point> pq = new PriorityQueue<>();
    static int n, m;
    boolean[][] visited;
    
    public void deepCopy() {
        
    }
    
    public void levitation() {
        for (int row = n-2; row >= 0; row--) {
            for (int col = 0; col < n; col++) {
                if (matrix[row][col] <= -1) {
                    continue;
                }
                int temprow = row;
                while (temprow != n-1) {
                    if (matrix[temprow + 1][col] >= -1) {
                        break;
                    }
                    matrix[temprow + 1][col] = matrix[temprow][col];
                    matrix[temprow][col] = -2;
                    temprow++;
                }
            }
        }
    }
    
    public void lotation() {
        int[][] newM = new int[n][n];
        
        for (int c = 0; c < n; c++) {
            for (int r = 0; r < n; r++) {
                newM[n-r-1][c] = matrix[c][r];
            }
        }
        
        matrix = newM;
    }
    
    public void bfs(int r, int c) {
        int block = matrix[r][c];
        visited[r][c] = true;
        PriorityQueue<Point> tempq = new PriorityQueue<>();
        
        Deque<Point> queue = new LinkedList<>();
        queue.add(Point.create(r, c));
        tempq.add(Point.create(r, c));
        boolean[][] zeroVis = new boolean[n][n];
        
        while (!queue.isEmpty()) {
            Point curPoint = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nr = curPoint.row + dr[i];
                int nc = curPoint.col + dc[i];
                
                if (!Point.valid(nr, nc)) {
                    continue;
                }
                
                if ((matrix[nr][nc] == 0 && !zeroVis[nr][nc]) || (matrix[nr][nc] == block && !visited[nr][nc])) {
                    tempq.add(Point.create(nr, nc));
                    queue.add(Point.create(nr, nc));
                    if (matrix[nr][nc] == 0) {
                        zeroVis[nr][nc] = true;
                    } else {
                        visited[nr][nc] = true;
                    }
                }
            }
        }
        if (tempq.size() < 2) {
            return;
        }
        
        if (tempq.size() > pq.size() || (tempq.size() == pq.size() && tempq.peek().compareTo(pq.peek()) > 0)) {
            pq = tempq;
        }
        return;
    }
    
    public void blank() {
        while (!pq.isEmpty()) {
            Point p = pq.poll();
            matrix[p.row][p.col] = -2;
        }
    }
    
    public void show() {
        for (int i = 0 ; i <n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.printf("%3d", matrix[i][j]);
            }
            System.out.println("");
        }
        System.out.println("");
    }
    
    public void solve() throws Exception {
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		matrix = new int[n][n];
		
		for (int i = 0; i < n; i++) {
		    st = new StringTokenizer(br.readLine());
		    for (int j = 0; j < n; j++) {
		        matrix[i][j] = Integer.parseInt(st.nextToken());
		    }
		}
		int ans = 0;
		while(true) {
		    visited = new boolean[n][n];
		    for (int r = 0; r < n; r++) {
		        for (int c = 0; c < n; c++) {
		            if (visited[r][c] || matrix[r][c] <= 0) {
		                continue;
		            }
		            bfs(r, c);
		        }
		    }
		    if (pq.size() == 0) {
		        break;
		    }
		    ans += (pq.size() * pq.size());
		    blank();
		    show();
		    levitation();
		    show();
		    lotation();
		    show();
		    levitation();
		    show();
		}
		System.out.println(ans);
    }
    
	public static void main(String[] args) throws Exception {
	    new Main().solve();
	}
	
	public static class Point implements Comparable<Point> {
	    int row;
	    int col;
	    
	    private Point(int row, int col) {
	        this.row = row;
	        this.col = col;
	    }
	    
	    static Point create(int row, int col) {
	        return new Point(row, col);
	    }
	    
	    static boolean valid(int row, int col) {
	        return !(row < 0 || row >= n || col < 0 || col >= n);
	    }
	    
	    @Override
    	public int compareTo(Point o) {
    		if (row < o.row) {
    		    return 1;
    		} else if (row > o.row) {
    		    return -1;
    		}
    		
    		if (col < o.col) {
    		    return 1;
    		}
    		return -1;
    	};
	}
	
	
}
