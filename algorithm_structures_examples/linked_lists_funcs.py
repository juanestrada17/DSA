class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_nth_node(head, n):
    counter = 1
    while counter < n:
        head = head.next
        counter += 1
    return head


def delete_nth_node(head, n):
    counter = 1
    pointer = head
    prev_last = ListNode()
    while counter < n:
        prev_last = pointer
        pointer = pointer.next
        counter += 1
    
    prev_last.next = pointer.next
    pointer.next = None
    return head

def reverse_llist(head):
    temp = None 
    while head:
        prev_next = head.next # 2 
        head.next = temp # None
        temp = head # 1 
        head = prev_next # 2 
    return temp