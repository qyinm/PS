class Solution {
    int[] answer = new int[2];
    int[][] quad;
    public int[] solution(int[][] arr) {
        quad = arr;

        recur(0, 0, arr.length/2);
        return answer;
    }
    
    public int recur(int y, int x, int n) {
        if (n == 0) {
            answer[quad[y][x]]++;
            return quad[y][x];
        }
        
        int ans = recur(y, x, n/2) + recur(y, x+n, n/2) + recur(y+n, x, n/2) + recur(y+n, x+n, n/2);
        // System.out.println(answer[0]);
        if (ans == 0) {
            answer[0]-=3;
            return 0;
        } else if (ans == 4) {
            answer[1]-=3;
            return 1;
        }
        return 100;
    }
}
