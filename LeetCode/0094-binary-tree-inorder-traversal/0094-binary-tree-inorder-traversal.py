# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.inord(ans, root)

        return ans

    def inord(self, ans, root: Optional[TreeNode]):
        if root == None:
            return
        self.inord(ans, root.left)
        ans.append(root.val)
        self.inord(ans, root.right)