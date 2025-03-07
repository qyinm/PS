class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        dp[0] = 1
        for st in range(2, n+1):
            dp[st] = dp[st-1] + dp[st-2]
        return dp[n]