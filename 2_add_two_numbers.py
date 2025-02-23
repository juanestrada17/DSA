class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next 


def print_node_vals(head):
    curr = head 
    
    while curr: 
        print(curr.val)
        curr = curr.next
        
def create_node(list): 
    head = ListNode(list[0])
    curr = head 
    
    for el in list[1:]:
        curr.next = ListNode(el)
        curr = curr.next
    return head

# head1 = create_node([9,9,9,9,9,9,9])
# head2 = create_node([9,9,9,9])


head1 = create_node([2,4,3])
head2 = create_node([5,6,4])
# Objective = return the sum of two linked list numbers
# that are reversed. The sum must be returned as a linked list
# Example = [2,4,3]
#           [5,6,4]
#      res = 342 + 465 = 807 


# We need a dummy list to which to append the res 
dummy = ListNode()
tail = dummy # actual res
# We need to calculate the carry 
carry = 0
current_sum = 0  
# We check carry since one list can reach its end before the other one. 
while head1 or head2 or carry:
    # We add the carry if there's one 
    current_sum = carry
    
    if head1: 
        #advance head1 only if it's still Truthy
        current_sum += head1.val
        head1 = head1.next
    if head2: 
        # adance head2 only if it's still possible
        current_sum += head2.val
        head2 = head2.next
    carry = current_sum // 10 
    current_sum = current_sum % 10
    tail.next = ListNode(current_sum)
    tail = tail.next
print_node_vals(dummy.next)
    




            

# 2 + 5 = 7 
# 4 + 6 = 10 -> carry 
# 3 + 4 = 7 + 1 = 8 




















# Solution if res not linked list

# def reverse_list(head):
#     temp = None
#     curr = head
#     while curr: 
#         prev_next = curr.next # 1-> 2
#         curr.next = temp # 1-> None
#         temp = curr # None -> 1 
#         curr = prev_next
#     return temp

# reversed_1 = reverse_list(head1)
# reversed_2 = reverse_list(head2)

# def find_num(head):
#     curr = head
#     res = 0

#     while curr: 
#         res = (res * 10) + curr.val
#         curr = curr.next
#     return res 

# res = find_num(reversed_1) + find_num(reversed_2)

# print(res)



