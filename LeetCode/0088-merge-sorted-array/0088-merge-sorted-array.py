class Solution:


    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ans = nums1[:m] + nums2[:]
        print(ans)

        for i in range(m, n+m):
            nums1[i] = nums2[i-m]

        for i in range(n+m):
            for j in range(i+1, n+m):
                if nums1[i] > nums1[j]:
                    nums1[i], nums1[j] = nums1[j], nums1[i]
        

    
        