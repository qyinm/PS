class Solution {
    fun containsNearbyDuplicate(nums: IntArray, k: Int): Boolean {
        val window = mutableSetOf<Int>()
        
        nums.forEachIndexed { i, num ->
            if (num in window) return true
            window.add(num)
            if (window.size > k) {
                window.remove(nums[i - k])
            }
        }
        
        return false
    }
}