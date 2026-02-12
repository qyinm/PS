class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        change_index = 0

        for new_index in range(1, len(nums)):
            if nums[change_index] != nums[new_index]:
                nums[change_index + 1] = nums[new_index]
                change_index += 1
        
        return change_index + 1