class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:    
        # 0 - 1 - 2 - 3     3 - 2 - 1 - 0 
        prev = None
        curr = head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev