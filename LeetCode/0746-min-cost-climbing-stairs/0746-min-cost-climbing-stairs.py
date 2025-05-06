class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [1e9] * (n + 1)

        memo[0] = memo[1] = 0

        for i in range(2, n + 1):
            memo[i] = min(memo[i-2] + cost[i-2], memo[i-1] + cost[i-1])
        
        return memo[n]