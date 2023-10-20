import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        Queue<Integer> process = new LinkedList<>();
        
        Arrays.stream(priorities).forEach(el -> pq.add(el));
        int n = priorities.length;
        IntStream.range(0, n).forEach(el -> process.add(el));
        
        while(!process.isEmpty()) {
            int curr = process.poll();
            if (pq.peek() > priorities[curr]) {
                process.add(curr);
                continue;
            }
            answer++;
            pq.poll();
            if (curr == location) {
                break;
            }
        }
        
        return answer;
    }
}
