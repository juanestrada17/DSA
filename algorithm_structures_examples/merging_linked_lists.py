
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

l1 = create_node([1,2,3])
l2 = create_node([4,5,6])

def merge_unsorted_lists(l1,l2):
    dummy = ListNode()
    dummyPointer = dummy
    toggle = True
    while l1 and l2: 
        if toggle: 
            dummyPointer.next = l1
            l1 = l1.next
        else:
            dummyPointer.next = l2 
            l2 = l2.next
        dummyPointer = dummyPointer.next
        # Switch toggle
        toggle = not toggle
    
    # Make sure the list that ends up with remaining elements gets added 
    dummyPointer.next = l1 or l2 # l1 if l1 else l2
    return dummy.next
print(merge_unsorted_lists(l1,l2).next.next.next.val)