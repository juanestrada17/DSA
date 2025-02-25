# Doubly linked list: each node contains a data element and two links pointing to the next
# and previous node

# Node of a doubly linked list
class Node:
    def __init__(self, next=None, prev=None, data=None):
        # reference to next node in DLL
        self.next = next
        # reference to previous node in DLL
        self.prev = prev
        self.data = data

def traverse(head):
    current = head
    while current: 
        current = current.next
        
def insert_at_beggining(head, value):
    new_node = Node(value)
    new_node.next = head
    head.prev = new_node
    return new_node
   
def insert_after_node(node, value):
    if node is None:
        print("Node is None")
        return
    
    new_node = Node(value)
    new_node.prev = node
    new_node.next = node.next
    
    # Update the prev of the node that was
    # previously there
    if node.next:
        node.next.prev = new_node
    
    node.next = new_node

def insert_before_node(node, value):
    if node is None:
        print('Node is None')
        return 
    
    # Create node
    new_node = Node(value)
    # set prev to the node's prev element
    new_node.prev = node.prev
    # set next to the node, since we are inserting before
    new_node.next = node
    
    if node.prev: 
        node.prev.next = new_node
    
    node.prev = new_node
    
def insert_at_end(head, value):
    if head is None: 
        print('Head is none')
        
    new_node = Node(value)
    current = head
    
    # Traverse till the end of linked list
    while current: 
        current = current.next
    
    # re-assign references 
    current.next = new_node
    new_node.prev = current
    return head

def delete_from_start(head):
    if head is None:
        return None
    
    if head.next is None: 
        return None 
    
    new_head = head.next
    new_head.prev = None
    # Make sure we remove all references in memory from head 
    del head 
    return new_head

# Traverse to the node, and delete it while re-adjusting the prev and next of its neighbors
def delete_node(head, position):
    if head is None:
        print('list is empty') 
        return None
    
    # If it's the first element we set its next element's prev
    # to None, deleting the first one
    if position == 0:
        if head.next:
            head.next.prev = None
        return head.next
    
    # Pointer 
    current = head
    count = 0 
    # Traverse to the Node 
    while current and count < position:
        current = current.next
        count += 1
        
    # out of range
    if current is None:
        return head
       
    # adjust the reference of the elements before and after the deleted node 
    if current.next: 
        current.next.prev = current.prev
    if current.prev:
        current.prev.next = current.next
    
    # Deletes the node from memory
    del current
    
    return head
    
def delete_node_end(head):
    if head is None:
        return None 
    
    # Pointer
    current = head  
    # With this logic we make sure that the loop ends when the node is the second to last.
    while current.next.next:
        current = current.next
    
    # Since current is the second to last, we set its next to None, and delete the node from memory using del 
    del_node = current.next
    current.next = None
    del del_node
    return head 