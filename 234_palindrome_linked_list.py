class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(head):
    
    curr = head 
    while curr:
        print(curr.val)
        curr = curr.next
        

def create_node(list):
    
    head = Node(list[0])
    crr = head
    
    for el in list[1:]:
        crr.next = Node(el)
        crr = crr.next
        
    return head

list = [1,2,2,1]
head = create_node(list)
# Find mid 
def find_mid(head):
    slow, fast = head, head 
    
    while fast and fast.next: 
        fast = fast.next.next
        slow = slow.next
        
    return slow
# Reverse elements

def reverse_linked_list(head): 
    new_next = None
    while head: 
        prev_next = head.next # 1 -> 2
        head.next = new_next # 1 -> none
        new_next = head # 1 
        head = prev_next # 2 
    return new_next

def compare_linked_lists(list1, list2):
    while list2: 
        if list1.val != list2.val:
            return False
        
        list1 = list1.next
        list2 = list2.next
    
    return True
    
def isPalindrome(head):
    mid = find_mid(head)
    reversed_list = reverse_linked_list(mid)
    return compare_linked_lists(head, reversed_list)


# Stack approach -> 2 passes 
def isPalindromeStack(head):
    stack = []
    curr = head 
    
    while curr:
        # Add values to stack 
        stack.append(curr.val)
        curr = curr.next
    
    curr = head
    while stack:
        # Compare first element with last element, pop the last element and traverse to the next
        if curr.val != stack.pop():
            return False
        curr = curr.next
    return True



