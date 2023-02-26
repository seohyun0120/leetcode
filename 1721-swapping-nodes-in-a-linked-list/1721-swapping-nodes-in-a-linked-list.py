# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        curr = head
        first = head
        second = head

        # k까지 탐색
        for _ in range(1, k):
            # 한 칸씩 전진
            curr = curr.next

        first = curr

        # k부터 끝까지 탐색
        while curr.next:
            curr = curr.next
            # 전체 길이 - k번째 노드 찾음
            second = second.next

        temp = first.val
        first.val = second.val
        second.val = temp

        return head