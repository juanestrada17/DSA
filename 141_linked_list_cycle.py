from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Set solution
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        res = set()
        while head:
            if head in res:
                return True
            else: 
                res.add(head)
            head = head.next
        return False
# Floyd cycle detection

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Both pointers start at the head 
        fast, slow = head, head 
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
         
        return False 
        
        