# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = deque()
        q.append(root)
        ans = []
        while q:
            n = len(q)
            ans.append(q[0].val)
            for _ in range(n):
                curr = q.popleft()
                if curr.right is not None:
                    q.append(curr.right)
                if curr.left is not None:
                    q.append(curr.left)
        return ans
        