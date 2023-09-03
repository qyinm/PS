import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        int n = progresses.length;
        int i = 0;
        int day = 0;
        while (i < n) {
            int cnt = 1;
            day += (int)Math.ceil((double)(100-progresses[i] - day * speeds[i]) / (double)speeds[i]);
            i++;
            while (i < n && progresses[i] + day * speeds[i] >= 100) {
                i++;
                cnt++;
            }
            answer.add(cnt);
        }
        int[] ans = answer.stream().mapToInt(Integer::intValue).toArray();
        return ans;
    }
}
