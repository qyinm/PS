class Solution {
    fun isHappy(n: Int): Boolean {
        val seen = hashSetOf<Int>()
        var current = n
        while (current > 9 && current !in seen) {
            seen.add(current)
            current = getNextNumber(current)
        }
        
        return current == 1
    }

    private fun getNextNumber(n: Int): Int {
        var sum = 0
        var num = n

        while (num > 0) {
            val digit = num % 10
            sum += digit * digit
            num /= 10
        }

        return sum
    }
}