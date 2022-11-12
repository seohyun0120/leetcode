# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, res):
            if not root:
                return

            if not root.left and not root.right:
                res.append(root.val)
                return
            dfs(root.left, res)
            dfs(root.right, res)
            
            return
        
        leaf1 = []
        dfs(root1, leaf1)

        leaf2 = []
        dfs(root2, leaf2)
        print(leaf1, leaf2)
        return leaf1 == leaf2