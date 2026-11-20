class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(-1) 
        prev = dummy
        prev.next = head
        curr = head
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next  
            else:
                prev = prev.next  
            curr = curr.next 
        
        return dummy.next