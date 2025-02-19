class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def list_to_head_node(list):
    head = ListNode(list[0])
    curr = head 
    for el in list[1:]:
        curr.next = ListNode(el)
        curr = curr.next
    return head 

list_head = [1,2,3,4,5]
head = list_to_head_node(list_head)

# Objective:
# Re-arrange a linked list
# L0 -> Ln -> L1 -> Ln - 1
# 1,2,3,4,5
# 1-> 5 -> 2 -> 4 -> 3 

# 1,2,3,4
# 1 -> 4 -> 2 -> 3
def reorder_list(head):
    reference_list = []
    curr = head
    # Remember we always do it over another linked list
    while curr:
        reference_list.append(curr)
        curr = curr.next
    
    start = 0 
    end = len(reference_list) - 1
    
    while start < end:
        prev_start_next = reference_list[start].next
        reference_list[start].next = reference_list[end]
        start += 1
        # For even len lists such as [1,2,3,4]
        if start >= end:
            break 
        reference_list[end].next = prev_start_next

        end -= 1
    reference_list[end].next = None
    return head

# Alternative solution using middle
# Find the middle -> Using slow and fast pointers
# Reverse the second half 
# Merge the two halves
         
def reorder_list_middle(head):
    # Find the middle
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    # Reverse second half 
    prev, curr = None, slow.next
    slow.next = None
    while curr: 
        temp = curr.next
        curr.next = prev 
        prev = curr 
        curr = temp
    
    # Merge the two 
    first, second = head, prev
    while second: 
        temp1, temp2 = first.next, second.next
        first.next = second 
        second.next = temp1 
        first, second = temp1, temp2
        
# Find the mid 
def find_mid(head):
    # Set fast and slow to head 
    fast, slow = head, head 
    
    # While fast exists we advance pointers 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # We return slow, when fast reaches the end it means
    # slow is at the mid point of the linked list
    return slow

# Rotate array 
def rotate_linked_list(head):
    # [1,2,3,4,5]
    curr = None 
    while head:
        prev_next = head.next # 1 -> 2
        head.next = curr # 1 -> None
        curr = head # None -> 1 
        head = prev_next # move pointer to next
    return curr

mid_list = find_mid(head)
# print(rotate_linked_list(mid_list).next.val)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Merge two linked lists without a dummy
def merge_two_linked_lists(list1, list2):
    # If one list is empty, return the other
    if not list1: 
        return list2
    if not list2: 
        return list1

    # Determine the head of the merged list
    if list1.val <= list2.val:
        head = list1
        first, second = list1, list2
    else:
        head = list2
        first, second = list2, list1

    # Merge by alternating nodes
    while first and second:
        temp1 = first.next
        temp2 = second.next

        first.next = second  # Connect first list node to second
        if not temp1:  # If list1 is exhausted, append remaining list2
            break
        second.next = temp1  # Connect second list node to first
        
        first, second = temp1, temp2  # Move forward

    return head  # Return the head of the merged list
