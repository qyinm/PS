import java.util.*;
import java.util.stream.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Set<List<Integer>> list = new HashSet<>();
        Arrays.sort(nums);
        int n = nums.length;

        for (int i = 1; i < n-1; i++) {
            int left = i - 1;
            int right = i + 1;
            while (left >= 0 && right < n) {
                int sum = nums[left] + nums[i] + nums[right];
                if (sum == 0) {
                    list.add(Arrays.asList(nums[left], nums[right], nums[i]).stream().sorted().toList());
                    right += 1;
                    left -= 1;
                } else if (sum < 0) {
                    right += 1;
                } else {
                    left -= 1;
                }
            }
        }

        

        List<List<Integer>> answer = new ArrayList<>(list);


        return answer;
    }
}