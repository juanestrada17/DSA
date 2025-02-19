# Objective: remove nth node from the end of a list and 
# return head 

# Example = [1,2,3,4,5]
# n = 2 
# Output [1,2,3,5]

# Important ->
# We count positions, so we don't do 0 indexing. 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_node(list):
    head = ListNode(list[0])
    headPointer = head
    
    for el in list[1:]:
        headPointer.next = ListNode(el)
        headPointer = headPointer.next
    return head 

head = create_node([1,2])
n = 1

# Two pointer distance solution
# We have one pointer at the start of the linked list 
# We have another pointer at nth element of the linked list 
# We advance until the longest pointer is at the end 
# When it does, the element after n is the element to delete 

# def delete_node_end(head, n):
    
#     # Dummy node -> initialized with 0 -> head 
#     res = ListNode(0, head)
#     # used to traverse the linked list
#     dummy = res
    
#     # Moves head to nth node, so that there's delay between dummy and head
#     for _ in range(n):
#         head = head.next
        
#     # Head is the advanced node, so we loop until we 
#     # reach its end    
#     while head:
#         head = head.next
#         dummy = dummy.next
    
#     # Dummy will be pointing at the node before 
#     # The nth element to the end
#     # So we skip it
#     dummy.next = dummy.next.next
    
#     # We return res 
#     return res.next 
    
def delete_node_end(head, n):
    # Create a dummy node, it's initialized to 0 val next head
    res = ListNode(0, head)
    # We create a pointer to navigate the linked list
    # This pointer starts at 0 followed by head, it allows us to place it before the node to the delete (skip) 
    dummy = res
    
    # We move head to the nth element, so that it's the non-delayed node
    for _ in range(n):
        head = head.next
    
    # While head hasn't reached its end we advance both pointers 
    while head:
        dummy = dummy.next
        head = head.next
    
    # Current slow pointer represents the element before nth end, thus we set it's next to the node after the deleted one
    dummy.next = dummy.next.next
    
    # Returns head after changes
    return res.next
    

print(delete_node_end(head, n).val)
    
    





#  Solution using arrays -> Store ll references in a list 
# def store_references(ll_list):
#     references = []
#     while ll_list:
#         references.append(ll_list)
#         ll_list = ll_list.next
#     return references

# def delete_nth_from_end(head, n):
#     list = store_references(head)
#     l_len = len(list)
#     if l_len == n:
#         head = head.next
#     else:
#         popped_index = l_len - n 
#         prev_index = popped_index - 1
#         after_index = list[popped_index].next
#         list[popped_index] = None
#         list[prev_index].next = after_index
#     return head

# print(delete_nth_from_end(head, n))


    

        


