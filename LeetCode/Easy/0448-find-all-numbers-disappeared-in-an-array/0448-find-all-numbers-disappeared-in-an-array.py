class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sets = set(range(1, n + 1))

        for num in nums:
            if num in sets:
                sets.remove(num)
        
        return sorted(list(sets))