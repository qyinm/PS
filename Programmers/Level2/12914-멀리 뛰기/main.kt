class Solution {
    fun solution(n: Int): Long {
        var answer: Long = 0
        val MOD = 1234567
        
        var memo = mutableListOf(1L, 1L)
        
        for (i in 2..n) {
            var temp: Long = 0
            for (j in 1..2) {
                temp += memo[i-j]
            }
            memo.add(temp % MOD)
        }
        answer = memo[n]
        
        return answer
    }
}