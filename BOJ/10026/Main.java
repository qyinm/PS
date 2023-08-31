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
    
    boolean[][] visited;
    Map<Character, Integer> ans1 = new HashMap<>();
    Map<Character, Integer> ans2 = new HashMap<>();
    
    public void solution() throws Exception {
        n = Integer.parseInt(br.readLine());
        red = new char[n][n];
        nored = new char[n][n];
        visited = new boolean[n][n];
        
        for (int i = 0; i < n; i++) {
            char[] charArr = br.readLine().toCharArray();
            red[i] = charArr;
            for (int j = 0; j < n; j++) {
                if (charArr[j] == 'G') {
                    nored[i][j] = 'R';
                } else {
                    nored[i][j] = charArr[j];
                }
            }
        }
        
        

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j]) {
                    bfs(i, j, red[i][j], red);
                    ans1.put(red[i][j], ans1.getOrDefault(red[i][j], 0)+1);
                }
            }
        }
        visited = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j]) {
                
                    bfs(i, j, nored[i][j], nored);
                    ans2.put(nored[i][j], ans2.getOrDefault(nored[i][j], 0)+1);
                }
            }
        }
        
        System.out.print(ans1.entrySet().stream().map(el -> el.getValue()).reduce(0, Integer::sum));
        System.out.print(" ");
        System.out.print(ans2.entrySet().stream().map(el -> el.getValue()).reduce(0, Integer::sum));
    }
    
    public void bfs(int y, int x, char key, char[][] arr) {
        Deque<int[]> deque = new ArrayDeque<>();
        deque.add(new int[]{y, x});
        
        while(deque.size() > 0) {
            int[] point = deque.pollFirst();
            int cy = point[0];
            int cx = point[1];
            
            for (int i = 0; i < 4; i++) {
                int ny = cy + dy[i];
                int nx = cx + dx[i];
                if (ny < 0 || ny >= n || nx < 0 || nx >= n) continue;
                if (visited[ny][nx] || arr[ny][nx] != key)    continue;
                visited[ny][nx] = true;
                deque.add(new int[]{ny, nx});
            }
        }
    }
    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
    
}
