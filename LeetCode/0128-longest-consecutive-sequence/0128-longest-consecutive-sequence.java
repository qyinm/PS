import java.util.*;

class Solution {
    public int longestConsecutive(int[] nums) {
        Arrays.sort(nums);
        if (nums.length < 2) {
            return nums.length;
        }
        int maxLength = 1;
        int length = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i-1] + 1) {
                maxLength = Math.max(length, maxLength);
                length = 1;
                continue;
            }
            if (nums[i] == nums[i-1] + 1)
                length += 1;
        }
        maxLength = Math.max(length, maxLength);
        return maxLength;
    }
}