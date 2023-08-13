import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;


class Main {
    static char[][] jail;
    static int tc;
    static BufferedReader br;
    static int h, w;
    static int[][] visited;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, -1, 0, 1};
    static Queue<Pair> q;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        tc = Integer.parseInt(br.readLine());
        for (int i = 0; i < tc; i++) {
            st = new StringTokenizer(br.readLine());
            h = Integer.parseInt(st.nextToken());
            w = Integer.parseInt(st.nextToken());
            jail = new char[h][w];
            visited = new int[h][w];
            
            for (int j = 0; j < h; j++) {
                char[] inS = br.readLine().toCharArray();
                for (int k = 0; k < w; k++) {
                    jail[j][k] = inS[k];
                    if (jail[j][k] == '$')  q.add(new Pair(j, k));
                }
            }

            for (int j = 0; j < h; j++) {
                for (int k = 0; k < w; k++) {
                    System.out.print(jail[j][k]);
                }
                System.out.println("");
            }
        }
    }

    public static int bfs(int cnt) {
        
        
        while (!q.isEmpty()) {
            Pair point = q.poll();
            
        }
        return 0;
    }

    public static class Pair{
        int x, y;
        Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
