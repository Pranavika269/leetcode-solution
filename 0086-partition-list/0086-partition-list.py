# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        less = dummy1
        more = dummy2
        
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                more.next = head
                more = more.next
            head = head.next
        
        more.next = None
        less.next = dummy2.next
        
        return dummy1.next