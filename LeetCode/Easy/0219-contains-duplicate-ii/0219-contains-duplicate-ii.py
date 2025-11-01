from collections import deque


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        end = len(nums)
        windowq = deque(nums[:k+1])
        count_dict = Counter(windowq)
        if len(set(windowq)) != len(windowq):
            return True

        for i in range(k+1, end):
            byebye = windowq.popleft()
            count_dict[byebye] -= 1
            if count_dict[nums[i]] == 1:
                return True
            count_dict[nums[i]] += 1
            windowq.append(nums[i])

        return False