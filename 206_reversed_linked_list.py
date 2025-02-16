import collections
from typing import Optional


head = [1,2,3,4,5]

# Class 
class ListNode:
    def __init__(self, val: int, next: Optional['ListNode'] = None):
        self.val = val 
        self.next = next

def create_llist(list):
    # Declare its value 
    head = ListNode(list[0])
    curr = head 
    for val in range(1, len(list)): 
        # Create link
        curr.next = ListNode(list[val])
        # change current value
        curr = curr.next
    return head 

# Then return as list 
def reverse_linked_list(ll_head):
    res = collections.deque()
    while ll_head:
        res.appendleft(ll_head.val)
        ll_head = ll_head.next
    return list(res)
        
llistHead = create_llist(head)


# 1 - reference -> 2
# 2 - reference -> 3
# 3 - reference -> None

# 3 - reference -> 2 
# 2 - reference -> 1
# 1 - reference -> None

# head is 1 -> head becomes 2 -> next becomes current 
# head becomes 3 -> next becomes current

def reverse_return_llist(ll_head):
    curr = None 
    while ll_head:
        prev = ll_head.next
        ll_head.next = curr 
        curr = ll_head
        ll_head = prev
    return curr
        

def print_ll_list(ll_head):
    arr = []
    while ll_head:
        arr.append(ll_head.val)
        ll_head = ll_head.next
    return arr
                
reversed = reverse_return_llist(llistHead)

print(print_ll_list(reversed))
