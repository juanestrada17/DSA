# Tortoise and Hare algorithm 

# Steps -> 
# 1. Uses two pointers 
# Slow Pointer -> one at a time
# Fast Pointer -> two at a time


# If there's no cycle fast pointer will be null
# If there's a cycle the fast pointer will catch up to the slow pointer 

class ListNode:
    def __init__(self, val=0, next =None):
        self.val = val
        self.next = next
def hasCycle(head: ListNode) -> bool:
    # Both pointers start at the head
    slow, fast = head, head
    
    # Ensure that fast doesn't reach null, if it does return False
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next
        
        if slow == fast: # If they catch up 
            return True 
        
    return False