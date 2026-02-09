class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        answer = 0 if nums[0] == 0 else 1

        prev_num = nums[0]
        curr = 0 if nums[0] == 0 else 1
        for i in range(1, len(nums)):
            if nums[i] == 1 and prev_num == nums[i]:
                curr += 1
            elif nums[i] == 1:
                curr = 1
            else:
                curr = 0
            answer = max(curr, answer)
            prev_num = nums[i]

        return answer