import java.util.*;

class Solution {
    int ans;
    int[] dx = {-1, 0, 1, 0};
    int[] dy = {0, 1, 0, -1};
    int n;
    int m;
    int[][] board;
    char[][] map;
    int sy, sx, ly, lx, ey, ex;
    
    public int solution(String[] maps) {
        n = maps.length;
        m = maps[0].length();
        
        map = new char[n][m];
        
        init(maps);
        
        int l = bfs(sy, sx, ly, lx);
        if (l == -1)    return -1;
        int e = bfs(ly, lx, ey, ex);
        if (e == -1)    return -1;
        return l + e;
    }
    
    public int bfs(int starty, int startx, int endy, int endx) {
        board = new int[n][m];
        Deque<int[]> deque = new ArrayDeque<>();
        deque.addLast(new int[]{starty, startx});
        board[starty][startx] = 1;
        while (deque.size() > 0) {
            int[] p = deque.pollFirst();
            int cy = p[0];
            int cx = p[1];
            
            for (int i = 0; i < 4; i++) {
                int ny = cy + dy[i];
                int nx = cx + dx[i];
                
                if (ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
                if (map[ny][nx] == 'X' || board[ny][nx] != 0) {
                    continue;
                }
                board[ny][nx] = board[cy][cx] + 1;
                deque.addLast(new int[]{ny, nx});
                
            }
        }
        return board[endy][endx]-1;
    }
    public void init(String[] maps) {
        for (int i = 0; i < n; i++) {
            map[i] = maps[i].toCharArray();
        }
        findStart();
    }
    
    
    public void findStart() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (map[i][j] == 'S') {
                    sy = i;
                    sx = j;
                } else if (map[i][j] == 'L') {
                    ly = i;
                    lx = j;
                } else if (map[i][j] == 'E') {
                    ey = i;
                    ex = j;
                }
            } 
        }
    }
}
