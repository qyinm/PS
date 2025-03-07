class Solution:
    def divisorGame(self, n: int) -> bool:

        memo = [False for _ in range(n+1)]
        for i in range(2, n+1):
            for j in range(i-1, 0, -1):
                if i % j == 0:
                    memo[i] &= memo[i-j]
                memo[i] = not memo[i]
        print(memo)
        return memo[n]