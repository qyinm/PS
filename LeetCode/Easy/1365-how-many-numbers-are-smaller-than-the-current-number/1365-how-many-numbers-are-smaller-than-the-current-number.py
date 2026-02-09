from collections import Counter

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            curr = 0
            for comp_num in nums:
                if num > comp_num:
                    curr += 1
            
            answer.append(curr)
        
        return answer