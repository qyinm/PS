class Solution {
    public int solution(String dirs) {
        int answer = 0;
        char[] dirsArray = dirs.toCharArray();
        
        boolean[][][][] visited = new boolean[11][11][11][11];
        int[] point = new int[]{0, 0};
        for (int i = 0; i < dirs.length(); i++) {
            int[] next = move(dirsArray[i]);
            
            int nx = point[0] + next[0];
            int ny = point[1] + next[1];
            
            if (nx < -5 || nx > 5 || ny < -5 || ny > 5) continue;

            if (!(visited[point[1]+5][point[0]+5][ny+5][nx+5] || visited[ny+5][nx+5][point[1]+5][point[0]+5])) {
                answer++;
                visited[point[1]+5][point[0]+5][ny+5][nx+5] = true;
                visited[ny+5][nx+5][point[1]+5][point[0]+5] = true;
            }
            
            
            point[0] = nx;
            point[1] = ny;
            
        }
        return answer;
    }
    
    public int[] move(char dir) {
        if (dir == 'U') {
            return new int[]{0, 1};
        } else if (dir == 'D') {
            return new int[]{0, -1};
        } else if (dir == 'L') {
            return new int[]{-1, 0};
        } else {
            return new int[]{1, 0};
        }
    }
}
