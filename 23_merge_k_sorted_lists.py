import heapq
# Objective = Merge an array of sorted linked lists 
# 1 -> 1 ->  2 -> 3 -> 4 -> 4 -> 5 -> 6 
# lists = [[1,4,5], [1,3,4], [2,6]]
class Node: 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __lt__(self, other):
        return self.val < other.val

def create_node(list):
    head = Node(list[0])
    curr = head 
    for el in list[1:]:
        curr.next = Node(el)
        curr = curr.next
    return head   

def print_all(head):
    curr = head 
    while curr:
        print(curr.val)
        curr = curr.next

l1 = create_node([1,4,5])
l2 = create_node([1,3,4])
l3 = create_node([2,6])
lists = [l1,l2,l3]

def merge_sorted_lists(l1, l2):
    dummy = Node()
    tail = dummy
    while l1 and l2: 
        if l1.val < l2.val: 
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2 
    return dummy.next
# First approach, O (n Log k) takes longer because we do it in sequence, we could 2 two at the time
# def mergeKLists(lists):
#     if not lists: 
#         return None
    
#     if len(lists) == 1:
#         return lists[0]
    
#     first = lists[0]
#     second = lists[1]
#     cur_sorted = merge_sorted_lists(first, second)
#     for list in lists[2:]:
#         cur_sorted = merge_sorted_lists(list, cur_sorted)
#     return cur_sorted

# Second approach, two at the time 
def mergeKLists(lists):
    
    if not lists:
        return None
    
    while len(lists) > 1:
        mergedLists = []
        # 2 since we want it to advance two spaces for each iterationb
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            # handles case when second list doesn't exist 
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            mergedLists.append(merge_sorted_lists(l1, l2))
        # Adjusts the size of the lists with the new one with everything merged and re-start if the len is still more than 1 
        lists = mergedLists
    # The remaining element in lists 
    return lists[0]        
    

# res = mergeKLists(lists)

# Third approach - external solution - Using heap 

def mergeKListsHeap(lists):
    heap = []
    
    # Pushes head of each list into the heap
    for l in lists: 
        if l:
            heapq.heappush(heap, l)
            
    dummy = Node()
    tail = dummy
    
    # Extract the minimum node and add it to the result 
    while heap: 
        min_node = heapq.heappop(heap) # Pop smallest
        tail.next = min_node
        tail = tail.next
        
        if min_node.next:
            heapq.heappush(heap, min_node.next)
            
    return dummy.next 
            
resHeap = mergeKListsHeap(lists)
print_all(resHeap)

# We push all heads into the heap, the heapq stores them from smallest to largest 
# When we pop we are popping the smallest element, and if it exists replacing it with the next value of that linked list
# we add it each time to the dummy's tail
# Example execution for lists = [[1,4,5],[1,3,4],[2,6]] will be 
# [1,1,2] -> [4,1,2] -> [4,3,2] -> [4,3,6] -> [4, 4, 6] -> [5, 4, 6] -> [5, 6] -> [6] -> [] 
# When the heap is empty, we finish the process
    
     
    
    



