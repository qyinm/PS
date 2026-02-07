# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, leaf_arr: List[Int], node: Optional[TreeNode]):
        if node.left == None and node.right == None:
            leaf_arr.append(node.val)
            return

        if node.left != None:
            self.dfs(leaf_arr, node.left)
        if node.right != None:
            self.dfs(leaf_arr, node.right)
        
        return

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        arr1 = []
        arr2 = []
        self.dfs(arr1, root1)
        self.dfs(arr2, root2)

        if len(arr1) != len(arr2):
            return False

        return all(
            ar1 == ar2
            for ar1, ar2 in zip(arr1, arr2)
        )
            