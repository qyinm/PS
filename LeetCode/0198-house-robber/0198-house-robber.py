class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [0] * (n+3)

        for i in range(n-1, -1, -1):
            memo[i] = max(memo[i+2] + nums[i], memo[i+1])
        return memo[0]