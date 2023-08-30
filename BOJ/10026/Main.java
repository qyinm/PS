import java.util.stream.*;
import java.util.*;
import java.io.*;

public class Main
{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    int[] dy = {-1, 0, 1, 0};
    int[] dx = {0, 1, 0, -1};
    
    char[][] red;
    char[][] nored;
    int n;
    public void solution() {
        n = Integer.parseInt(br.readLine());
        red = new char[n][n];
        nored = new char[n][n];
        
        for (int i = 0; i < n; i++) {
            char[] charArr = br.readLine().toCharArray();
            for (int j = 0; j < n; j++) {
                if (charArr[j] == 'G') {
                    nored[i][j] = 'R';
                }
            }
        }
        
    }
    
    public void bfs(int y, int x) {
        Deque<int[]> deque = new ArrayDeque<>();
        deque.add(new int[]{y, x});
        
        while(deque.length > 0) {
            int[] point = deque.pollFirst();
            int cy = point[0];
            int cx = point[1];
            
            for (int i = 0; i < 4; i++) {
                int ny = cy + dy[i];
                int nx = cx + dx[i];
                if (ny < 0 || ny >= n || nx < 0 || nx >= n) continue;
                
            }
        }
    }
    public static void main(String[] args) {
        new Main().solution();
    }
    
}
