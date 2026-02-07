class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        prefix_dot = [nums[0]]
        for i in range(1, len(nums)):
            prefix_dot.append(prefix_dot[i - 1] * nums[i])
        
        suffix_dot = [nums[-1]]
        for i in range(1, len(nums)):
            suffix_dot.append(suffix_dot[i - 1] * nums[-i -1])

        suffix_dot = suffix_dot[::-1]

        for i in range(len(nums)):
            prefix_val = 1 if i - 1 < 0 else prefix_dot[i - 1]
            suffix_val = 1 if i + 1 >= len(nums) else suffix_dot[i + 1]

            answer.append(prefix_val * suffix_val)
        
        return answer   
