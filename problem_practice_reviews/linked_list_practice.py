# Linked list class 
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Doubly linked list
class DoublyNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class RandomNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val 
        self.next = next
        self.random = random

# Print all values from a linked list 
def print_all(head):
    current = head 
    while current: 
        print(current.val)
        current = current.next     
   
# Create a linked list from a list 
def create_linked_list(list):
    head = Node(list[0])
    current = head
    for el in list[1:]:
        current.next = Node(el)
        current = current.next
    return head 

testList = create_linked_list([1,2,3,4,5])


# Inserting at start of list 
def insert_linked_list(head, val):
    new_node = Node(val)
    new_node.next = head 
    return new_node

testListInsert = insert_linked_list(testList, 0)

# Traversing to a point in the list 
def traverse_to_node(head, val):
    current = head 
    while current and current.val != val:
        current = current.next
    return current

# Doubly linked list deletion of nodes 
def delete_node_doubly_list(node):
    if node is None:
        return None
    
    prev, next = node.prev, node.next
    next.prev = prev
    prev.next = next


# Reversing a linked list 
def reverse_linked_list(head):
    new_next = None
    while head: 
        prev_next = head.next
        head.next = new_next
        new_next = head 
        head = prev_next
    return new_next

# Merging linked lists  
list1 = create_linked_list([1,2,3])
list2 = create_linked_list([4,5,6,7])
def merge_sorted_llists(list1, list2):
    dummy = Node()
    tail = dummy
    
    while list1 and list2:  
        if list1.val < list2.val: 
            tail.next = list1 
            list1 = list1.next
        else: 
            tail.next = list2 
            list2 = list2.next
        # Advance the tail forward
        tail.next
    tail.next = list1 if list1 else list2 
    return dummy.next 

# Finding cycles on linked lists -> REMEMBER WE USE Floyd's algorithm /  Hare and tortoise 
def find_cycle(head):
    slow, fast = head, head 
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        
        if fast == slow:
            return True
    return False

# Finding cycles using a set 
def find_cycle_with_set(head):
    res = set()
    current = head 
    while current: 
        if current in res: 
            return True
        res.add(current)
        current = current.next
    return False

# Finding the mid of a list using two pointers 
def find_list_mid(head):
    slow, fast = head, head
    while fast and fast.next: 
        slow = slow.next
        fast = fast.next.next
    return slow

# Merge two linked lists alternating between nodes 
def merge_two_linked_lists(list1, list2):
    dummy = Node()
    tail = dummy
    list1Turn = True
    
    while list1 and list2: 
        if list1Turn:
            tail.next = list1
            list1 = list1.next
        else: 
            tail.next = list2
            list2 = list2.next
        tail = tail.next
        list1Turn = not list1Turn
    tail.next = list1 if list1 else list2
    return dummy.next

l1 = create_linked_list([1,2])
l2 = create_linked_list([5,4,3])
    
# Reordering a list so we alternate between first and last elements 
def reorder_list(head):
    # Find mid 
    mid = find_list_mid(head)
    second_half = mid.next
    mid.next = None
    # reverse after mid 
    second_half = reverse_linked_list(second_half)
    head = merge_two_linked_lists(head, second_half)
    return head 

# Have a delayed node and advanced node 
def remove_nth_from_end(head, n): 
    res = Node(0, head)
    dummy = res 
    
    for _ in range(n):
        head = head.next
    # Head is advanced
    while head: 
        head = head.next
        dummy = dummy.next
    # When head reaches end it means dummy is 
    # at the nth to the end element 
    dummy.next = dummy.next.next
    return res.next
removeTest = create_linked_list([1,2,3,4,5])
    
def add_two_numbers(l1, l2):
    dummy = Node()
    tail = dummy
    current_sum = 0 
    carry = 0
    while l1 or l2 or carry: 
        current_sum = carry 
        
        if l1:
            current_sum += l1.val
            l1 = l1.next
        if l2:
            current_sum += l2.val
            l2 = l2.next
            
        # Check if current sum exceeds 10 and calculate the carry 
        new_node = current_sum % 10 
        carry = current_sum // 10
    
        tail.next = Node(new_node)
        tail = tail.next
    return dummy.next

add_l1 = create_linked_list([2,4,3])
add_l2 = create_linked_list([5,6,4])
sum_ll = add_two_numbers(add_l1, add_l2)
# Expected output = [7,0,8]    

def find_dup(list):
    # Find cycle using hare and tortoise algorithm
    fast, slow = 0, 0 
    
    while True: 
        slow = list[slow]
        fast = list[list[fast]]
        
        if slow == fast: 
            break 
    # Beginning of the array 
    slow2 = 0 
    while True: 
        slow = list[slow]
        slow2 = list[slow2]
        
        if slow == slow2:
            return slow 
    
    