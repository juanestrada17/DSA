# n = length of linked list
# None of the pointers should remain in the newly created list
import copy
from typing import Optional
class Node: 
    def __init__(self, x:int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def linked_list_els(linkedListHead: Optional['Node']):
    arr = []
    while linkedListHead:
        arr.append(linkedListHead.val)
        linkedListHead = linkedListHead.next
    return arr

# Creates nodes and returns a dictionary with each node with their key as a value 
def create_nodes(list):
    dict = {}
    head = Node(x=list[0][0])
    # Value -> 1 
    dict[0] = head
    curr = head 
    for el in range(1, len(list)):
        curr.next = Node(list[el][0])
        dict[el] = curr.next
        curr = curr.next
    return dict, head  
# Takes those nodes and assigns them the reference by getting the reference node out of the dictionary 
def assign_rands(list, dict, head):
    curr = head
    for el in list:
        if el[1] == None:
            curr.random = None
        else:
            curr.random = dict[el[1]]
        curr = curr.next    
    return head


list= [[7,None],[13,0],[11,4],[10,2],[1,0]]
dict_vals, initial_nodes = create_nodes(list)
nodes_with_rands = assign_rands(list, dict_vals, initial_nodes)

head = nodes_with_rands

# First approach 
# Create a whole new linked list, as it's being created store the randoms and create a dict with references
# After it's created, we assign the randoms using the dictionary 
# return 

def deep_copy(head):
    current = head
    
    references = {}
    # original nodes = [7 - 13 - 11 - 4 - 2 - 1]
    # New nodes = [7 - 13 -11 -4 -2 -1]
    while current: 
        # We add original node as key, new node as value 
        references[current] = Node(current.val)    
        current = current.next 
    
    # We need another pass through head, 
    # Right now new nodes are not linked and they don't have randoms
    current = head 
    while current:
        references[current].next = references[current.next] if current.next else None
        references[current].random = references[current.random] if current.random else None
        current = current.next
    
    return references[head]

res = deep_copy(head)

# list= [[7,None],[13,0],[11,4],[10,2],[1,0]]
print(res)
# print(linked_list_els(res))


# Second approach 
# Create a copy of the node by using its value and set it to be the next of the original

# while head:
#     print(head.val)
#     head = head.next
    



# 1 -> 1 -> No next node 

# Set randoms by accessing the random of the original.next (This works because it's always after the original element)
# Detach the original from the newly created one, return. 
