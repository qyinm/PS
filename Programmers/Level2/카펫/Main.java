import java.util.*;

class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        
        int sum = brown + yellow;
        int sq = (int)Math.sqrt(sum);
        List<int[]> sizes = new ArrayList<>();
        
        for (int i = 1; i <= sq; i++) {
            if (sum % i == 0) {
                sizes.add(new int[]{sum/i, i});
            }
        }
        sizes.stream().forEach(size -> {
            if ((size[0]-2)*(size[1]-2) == yellow) {
                answer[0] = size[0];
                answer[1] = size[1];
            }
        });
        return answer;
    }
}
