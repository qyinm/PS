class Solution:
    def solve(self, s, i, j, dp) -> int:
        if i > j:
            return 0
        if i == j:
            return 1
        if dp[i][j] != -1:
            return dp[i][j]

        if s[i] == s[j]:
            dp[i][j] = 2 + self.solve(s, i+1, j-1, dp)
        else:
            dp[i][j] = max(self.solve(s, i+1, j, dp), self.solve(s, i, j-1, dp))
        return dp[i][j]
        
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        dp = [[-1] * n for _ in range(n)]
        
        return self.solve(s, 0, n-1, dp)
