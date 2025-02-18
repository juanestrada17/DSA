# Linked lists 
# Each element in the linked list is an object -> Box
# It contains 

# Python linked list ->  

from typing import Optional


class ListNode:
    def __init__(self, val: int, next: Optional['ListNode'] = None):
        self.val = val 
        self.next = next

# Create a linked list out of a list helper function
def create_linked_list(values):
    if not values:
        return None 
    # The first value of the array is the head
    head = ListNode(values[0])
    current = head 
    
    # Iterate over remaining values 
    for val in values[1:]:
        # Create the node with second value, and assign the pointer 
        # to the current node, in this case head
        current.next = ListNode(val)
        # Change the current node to the newly created one
        current = current.next
    return head

arr= [1,2,3]

# Linked lists are represented by their head, their starting point so to print them we have to access their head and loop
# Until it becomes None 
def linked_list_els(linkedListHead: Optional['ListNode']):
    arr = []
    while linkedListHead:
        arr.append(linkedListHead.val)
        linkedListHead = linkedListHead.next
    return arr

linked_list_head = create_linked_list(values=arr)
print(linked_list_els(linked_list_head))

# Dummy Nodes =>
# A temporary placeholder

# Slow pointers  vs. Fast Pointers
# Move 1 at time vs. Move 2 at time

# Finding middle in linked lists 
# When Fast pointers finish the end, slow pointers position represents end. 







# Linked list example in Java
# class Node{
#     int data -> data of current box
#     Node next -> reference to the next box in the list
#     Node(int data){
#       this.data = data
#     }
#   }

# Node nodeA = new Node(6)
# Node nodeB = new Node(3)
# Links
# nodeA.next = nodeB
# nodeB.next = nodeC


