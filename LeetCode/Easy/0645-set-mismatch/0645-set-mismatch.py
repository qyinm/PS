class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_check = [False] * (n + 1)
        num_check[0] = True

        for num in nums:
            if num_check[num] == False:
                num_check[num] = True
            else:
                dup_num = num
        
        for idx, val in enumerate(num_check):
            if val == False:
                missing = idx
                break
        
        return [dup_num, missing]
                