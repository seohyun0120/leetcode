# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        root = pre = ListNode(0)
        
        while head and head.next:
            temp = head.next
            
            # swap
            # 1 -> 2 / 2 -> 1
            head.next, temp.next = temp.next, head
            
            # pre
            # 0 -> 2 -> 1
            pre.next = temp
            
            # head 3 / pre 1
            head, pre = head.next, pre.next.next
        
        return root.next