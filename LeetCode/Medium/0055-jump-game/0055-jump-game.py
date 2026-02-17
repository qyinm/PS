from collections import deque

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        visited = set({0})
        qu = deque([0])
        n = len(nums) - 1

        while qu:
            curr = qu.popleft()
            rangeList = [curr + w + 1 for w in range(nums[curr])]

            for nextIdx in rangeList:
                if nextIdx >= n:
                    return True
                if nextIdx in visited:
                    continue
                qu.append(nextIdx)
                visited.add(nextIdx)
        
        return False