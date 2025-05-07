class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [0, 1, 1]

        for i in range(3, n+1):
            memo.append(memo[i-1] + memo[i-2] + memo[i-3])
        return memo[n]