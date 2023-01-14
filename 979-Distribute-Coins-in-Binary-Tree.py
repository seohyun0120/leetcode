# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)

        return self.res

    def dfs(self, root: Optional[TreeNode]):
        if not root:
            return 0
        
        left = self.dfs(root.left)
        self.res += abs(left)
        right = self.dfs(root.right)
        self.res += abs(right)

        return left + right + root.val - 1
