import java.util.*;
import java.io.*;
public class Main
{
    private static enum Direction {
        D,
        L;
    }
    // 우, 하, 좌, 상
    private int[][] direction = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    private int snakeDirection = 0;
    private int[][] graph;
    private int N;
    private Deque<int[]> snakeDeq = new ArrayDeque<int[]>();
    private int moveCount = 0;
    private BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private StringTokenizer st;
    
    private void changeDirection(Direction command) {
        switch(command) {
            case D:
                snakeDirection = (snakeDirection + 1) % 4;
                break;
            case L:
                snakeDirection = snakeDirection - 1 < 0 ? 3 : snakeDirection - 1;
                break;
        }
    }
    
    private boolean checkEnd(int[] point) {
        int row = point[0];
        int col = point[1];
        return row < 0 || row >= N || col < 0 || col >= N || graph[row][col] == -1;
    }
    
    // 움직인 곳에 사과가 있는지?
    private boolean checkApple(int[] point) {
        int row = point[0];
        int col = point[1];
        return graph[row][col] == 1;
    }
    
    private int[] movePoint(int[] point) {
        int row = point[0] + direction[snakeDirection][0];
        int col = point[1] + direction[snakeDirection][1];
        
        return new int[]{row, col};
    }
    // main logic
    // 이동에 성공하면 true, 못하면 false => 게임 끝
    private boolean move(int count) {
        for (int c = 0; c < count; c++) {
            // show();
            moveCount += 1;
            int [] head = movePoint(snakeDeq.peekLast());
            snakeDeq.addLast(head);
            
            if (checkEnd(head)) {
                return false;
            }

            if (!checkApple(head)) {
                int[] tail = snakeDeq.peekFirst();
                graph[tail[0]][tail[1]] = 0;
                snakeDeq.pollFirst();
            }
            graph[head[0]][head[1]] = -1;
        }
        return true;
    }
    
    private void show() {
        for (int[] gr: graph) {
            for (int g: gr) {
                System.out.print(g + " ");
            }
            System.out.println("");
        }
        System.out.println("");
    }
    
    private void solve() throws Exception {
        N = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());
        graph = new int[N][N];
        // 지렁이는 -1, 그냥 길은 0, 사과는 1
        graph[0][0] = -1;
        snakeDeq.addLast(new int[]{0, 0});
        // apple marking
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int appleRow = Integer.parseInt(st.nextToken()) - 1;
            int appleCol = Integer.parseInt(st.nextToken()) - 1;
            
            graph[appleRow][appleCol] = 1;
        }
        
        // show();
        int l = Integer.parseInt(br.readLine());
        for (int i = 0; i < l; i++) {
            st = new StringTokenizer(br.readLine());
            int cnt = Integer.parseInt(st.nextToken());
            Direction cmd = Direction.valueOf(st.nextToken());
            // 게임 끝날 시 프로그램 종료
            if (!move(cnt - moveCount)) {
                System.out.println(moveCount);
                return;
            }
            // 방향 전환
            changeDirection(cmd);
        }
        // 명령 다 수행하고 아직 종료 안되면 현재 방향으로 계속 진행
        for (int i = 1; move(i);) {}
        System.out.println(moveCount);
        // show();
    }

	public static void main(String[] args) throws Exception {
		new Main().solve();
	}
}
