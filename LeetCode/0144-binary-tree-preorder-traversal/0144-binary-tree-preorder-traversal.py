# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorder(self, node, answer):
        if node == None:
            return
        answer.append(node.val)
        self.preorder(node.left, answer)
        self.preorder(node.right, answer)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        self.preorder(root, answer)
        return answer
