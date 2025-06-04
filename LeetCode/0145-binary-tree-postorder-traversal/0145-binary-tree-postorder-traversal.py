# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def post(self, node, answer):
        if not node:
            return
        self.post(node.left, answer)
        self.post(node.right, answer)
        answer.append(node.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.post(root, ans)
        return ans