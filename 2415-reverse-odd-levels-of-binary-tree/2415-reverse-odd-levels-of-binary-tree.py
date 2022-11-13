# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        level = 0
        
        while q:
            if level % 2 != 0: # odd
                l = 0
                r = len(q) - 1
                
                while l < r:
                    q[l].val, q[r].val = q[r].val, q[l].val
                    l += 1
                    r -= 1
            
            for _ in range(len(q)):
                cur = q.popleft()

                if cur.left:
                    q.append(cur.right)
                if cur.right:
                    q.append(cur.left)

            level += 1

        return root