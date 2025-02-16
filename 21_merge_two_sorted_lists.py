list1 = [1,2,4]
list2 = [1,3,4]

# Objective = merge two lists into sorted 1 
# return the head 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def list_to_node(list):
    
    head = ListNode(list[0])
    current = head
    for val in list[1:]:
        current.next = ListNode(val)
        current = current.next
    return head 

l_list1 = list_to_node(list1)
l_list2 = list_to_node(list2)

def merge_arrs(l_list1, l_list2):
    dummy = ListNode()
    tail = dummy
    while l_list1 and l_list2:
        # If the head node of l1 is smaller than head node of l2
        if l_list1.val < l_list2.val:
            tail.next = l_list1
            l_list1 = l_list1.next
        else:
            tail.next = l_list2
            l_list2 = l_list2.next
        tail = tail.next # move tail forward
        
    tail.next = l_list1 if l_list1 else l_list2

    return dummy.next
print(merge_arrs(l_list1, l_list2).val)

