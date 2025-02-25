# Create an LRU cache

# Base knowledge to solve it -> Doubly linked list: each node contains a data element and two links pointing to the next
# and previous node

# Node of a doubly linked list
class Node:
    def __init__(self, data=None, next=None, prev=None, ):
        # reference to next node in DLL
        self.next = next
        # reference to previous node in DLL
        self.prev = prev
        self.data = data
        
def create_ddl_from_list(list):
    head = Node(list[0])
    curr = head
    for el in list[1:]:
        new_node = Node(el)
        curr.next = new_node
        new_node.prev = curr    
        curr = curr.next
    return head

def print_all_vals(head):
    current = head
    while current:
        print(current.data)
        current = current.next
        


ddl = create_ddl_from_list([1,2,3,4,5])
# Objetive => 
# It has a capacity 

# When we call the put to add a new element to the cache we have to make it the most used, shifting it to the head
# When we call the get, we make that element the most used 
# Example 

# Capacity is 2 
# put -> [2,2] Latest is 2,2 (Head, most recently used)
# put -> [3,3] Latest is 3,3 (head, most recently used)
# put -> [1,1] add [1,1] to head -> Pop last element from array

# Capacity is 2 
# put -> [2,2] Latest is 2,2 (Head, most recently used)
# put -> [3,3] Latest is 3,3 (head, most recently used)
# get -> [2,2] latest is 2,2 


# TODO -> Create a method to delete the node with a certain key  """ DONE """" 
# TODO -> Create a way to insert a key to the beginning of the DLL -> When we perform put we use this method """ DONE """
# TODO -> merge delete node + append beggining -> when we perform GET we use this method 
# TODO -> Have a conditional that checks if the capacity is exceeded 
# TODO -> If capacity is exceeded we append new node, delete last node 
# Do we need a hash map storing the keys and their references?


def delete_last_node(head):
    if head is None:
        return None
    
    if head.next is None:
        return None
    # get the element before the last 
    current = head 
    # Traverse till we get to the previous to last 
    while current.next.next: 
        current = current.next
        
    del_node = current.next
    current.next = None
    del del_node
    return head

def delete_node_key(head, key):
    if head is None: 
        return None
    
    current = head
    # We pass current to handle case when key is not in he list 
    while current and current.data != key:
        current = current.next
        
    # handles case when the deleted element is the head
    if current == head: 
        head = current.next
    
    
    if current.next: 
        current.next.prev = current.prev
    if current.prev:
        current.prev.next = current.next
        
    del current
        
    return head 
    

def insert_ddl_start(head, value):
    if head is None:
        return None
    
    new_node = Node(value)
    new_node.next = head
    head.prev = new_node
    return new_node
    
# the key becomes the most recently used 
# 1. We delete the element with the delete_node_key
# 2. we insert it to the start of the list  
def get(ddl, key):
    deleted_key = delete_node_key(head=ddl,key=key)
    updated_ddl = insert_ddl_start(head=deleted_key, value=key)
    return updated_ddl

# if we don't exceed capacity 
# insert beginning 
def put(key, value, capacity):
    
    pass

res = get(ddl, 5)
      

# deleted_val = delete_last_node(ddl)




