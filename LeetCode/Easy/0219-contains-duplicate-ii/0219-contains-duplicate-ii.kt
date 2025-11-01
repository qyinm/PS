class Solution {
    fun containsNearbyDuplicate(nums: IntArray, k: Int): Boolean {
        val window = HashSet<Int>()
        
        for (i in nums.indices) {
            if (nums[i] in window) {
                return true
            }
            window.add(nums[i])
            if (window.size > k) {
                window.remove(nums[i - k])
            }
        }
        
        return false
    }
}