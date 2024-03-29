import java.util.*;
import java.io.*;

public class Main
{
    int[][] matrix;
    int[] dr = {-1, 0, 1, 0};
    int[] dc = {0, 1, 0, -1};
    Deque<Point> pq = new LinkedList<>();
    int rainbow = 0;
    static int n, m;
    boolean[][] visited;
    
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
        Deque<Point> tempq = new LinkedList<>();
        
        Deque<Point> queue = new LinkedList<>();
        queue.add(Point.create(r, c));
        tempq.add(Point.create(r, c));
        boolean[][] zeroVis = new boolean[n][n];
        int tempRainbow = 0;
        while (!queue.isEmpty()) {
            Point curPoint = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nr = curPoint.row + dr[i];
                int nc = curPoint.col + dc[i];
                
                if (!Point.valid(nr, nc) || matrix[nr][nc] < 0) {
                    continue;
                }
                
                if ((matrix[nr][nc] == 0 && !zeroVis[nr][nc]) || (matrix[nr][nc] == block && !visited[nr][nc])) {
                    tempq.add(Point.create(nr, nc));
                    queue.add(Point.create(nr, nc));
                    if (matrix[nr][nc] == 0) {
                        tempRainbow += 1;
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
        
        if (tempq.size() > pq.size()) {
            rainbow = tempRainbow;
            pq = tempq;
            return;
        }
        
        if (tempq.size() < pq.size()) {
            return;
        }
        
        if (tempRainbow < rainbow) {
            return;
        }
        if (tempRainbow > rainbow) {
            rainbow = tempRainbow;
            pq = tempq;
            return;
        }
        
        if (tempq.peekFirst().compareTo(pq.peekFirst()) > 0) {
            rainbow = tempRainbow;
            pq = tempq;
            return;
        }
        
    }
    
    public void blank() {
        rainbow = 0;
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
		    if (pq.isEmpty()) {
		        break;
		    }
		    ans += (pq.size() * pq.size());
		    blank();
		    //show();
		    levitation();
		    //show();
		    lotation();
		    //show();
		    levitation();
		    //show();
		}
		System.out.println(ans);
    }
    
	public static void main(String[] args) throws Exception {
	    new Main().solve();
	    /*
	    PriorityQueue<Point> pq = new PriorityQueue<>();
	    pq.add(Point.create(4, 1));
	    pq.add(Point.create(3, 4));
	    Point p = pq.poll();
	    Point p2 = pq.poll();
	    if (p.compareTo(p2) > 0) {
	        System.out.println(p.row + " " + p.col);
	    } else {
	        System.out.println(p2.row + " " + p2.col);
	    }
	    */
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
    		if (row == o.row) {
    		    return col - o.col;
    		}
    		return row - o.row;
    	}
	}	
}
