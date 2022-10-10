# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head
        p2 = head.next
        cur = 0
        
        while p2:
            if p2.val == 0:
                p1 = p1.next
                p1.val = cur
                cur = 0
            
            else:
                cur += p2.val
            
            p2 = p2.next
        
        p1.next = None
    
        return head.next
        