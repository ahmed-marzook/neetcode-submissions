# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced, height = self.dfs(root)
        return balanced
    
    def dfs(self, root: Optional[TreeNode]):
        if not root:
            return True, 0
        lb, lefth = self.dfs(root.left)
        rb, righth = self.dfs(root.right)
        balanced = lb and rb and abs(lefth - righth) <= 1
        return balanced, 1 + max(lefth, righth)