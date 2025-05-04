from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, node):
        if node == None:
            return 0
        return 1 + max(self.dfs(node.right), self.dfs(node.left))
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
        