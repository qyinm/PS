import java.util.*;

class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int maxNum = 0;
        for (int candy: candies) {
            maxNum = Math.max(maxNum, candy);
        }
        List<Boolean> answer = new ArrayList<>();
        for (int candy: candies) {
            answer.add(maxNum <= candy + extraCandies);
        }
        return answer;
    }
}