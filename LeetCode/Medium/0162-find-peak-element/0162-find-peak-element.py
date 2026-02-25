class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        lo, hi = 0, n - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            left_val = float('-inf') if mid == 0 else nums[mid - 1]
            right_val = float('-inf') if mid == n - 1 else nums[mid + 1]
            peak_range = [left_val, nums[mid], right_val]

            print(mid)

            if max(peak_range) == nums[mid]:
                return mid

            if max(peak_range) == left_val:
                hi = mid - 1
            else:
                lo = mid + 1

        return 0