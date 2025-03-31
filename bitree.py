class Node: 
    def __init__(self, data=None, next=None): 
        self.data = data 
        self.next = next
        
def reverseList(node):
    revList = None
    while node:
        prevNext = node.next
        node.next = revList
        revList = node 
        node = prevNext
    return revList

def findMid(head):
    slow, fast = head, head
    while fast and fast.next: 
        slow = slow.next
        fast = fast.next.next
        
    return slow  

def findCycle(head):
    slow, fast = head, head
    while fast and fast.next: 
        slow = slow.next
        fast = fast.next.next
        if slow == fast: 
            return True
    return False

def mergeSorted(l1, l2): 
    dummy = Node()
    tail = dummy
    
    while l1 and l2: 
        if l1.data < l2.data: 
            tail.next = l1 
            l1 = l1.next
        else: 
            tail.next = l2 
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2 
    
    return dummy.next 

def mergeTwo(l1, l2):
    dummy = Node()
    tail = dummy 
    l1Turn = True
    
    while l1 and l2: 
        if l1Turn: 
            tail.next = l1 
            l1 = l1.next
        else: 
            tail.next = l2 
            l2 = l2.next
        tail = tail.next 
        l1Turn = not l1Turn
    tail.next = l1 if l1 else l2 
    return dummy.next 

def reOrderList(head):
    # first and last element 
    
    # find mid 
    mid = findMid(head)
    # separate first and second half 
    secondHalf = mid.next
    mid.next = None
    
    # reverse second half
    revSecondH = reverseList(secondHalf) 
    # merge first and rev second half 
    
    head = mergeTwo(head, revSecondH)
    
    return head 

# adv and del 
def removeNthEl(head, n):
    # delayed 
    dummy = Node(0, head)
    tail = dummy
    
    # advanced 
    for _ in range(n): 
        head = head.next
    
    # advance both 
    while head: 
        head = head.next
        tail = tail.next
    
    # When head reaches end tail will be before n element 
    tail.next = tail.next.next
    
    return dummy.next 

# create a deep copy, it has next and random pointers 
def randPointers(head):
    references = {}
    
    current = head 
    while current: 
        references[current] = Node(current.data)
        current = current.next
    
    # second pass to assign next and rands 
    current = head 
    while current: 
        if current.next: 
            references[current].next = references[current.next]
        if current.random: 
            references[current].random = references[current.random]
        current = current.next
    return references[head]

def addTwoNums(l1, l2):
    # Create a new ll with the res 
    dummy = Node()
    tail = dummy
    # carry 
    carry = 0 
    # current sum
    currentSum = 0 
    while l1 or l2 or carry: 
        currentSum = carry 
        if l1: 
            currentSum += l1.data 
            l1 = l1.next
        elif l2: 
            currentSum += l2.data
            l2 = l2.next
         
        carry = currentSum // 10
        remainder = currentSum % 10
        
        tail.next = Node(remainder)
        tail = tail.next
    return dummy.next 

# Floyds algo
def findDup(list):
    # Find cycle 
    slow, fast = 0, 0 
    
    while True: 
        slow = list[slow]
        fast = list[list[fast]]
        
        if slow == fast: 
            break 
    
    # find cycle entrance, dup 
    slow2 = 0 
    
    while True: 
        slow = list[slow]
        slow2 = list[slow2]
        
        if slow == slow2: 
            return slow2 
        

def mergeKSorted(lists):
    
    while len(lists) > 1:
        mergedLists = []
        # advance in two 
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            
            mergedLists.append(mergeSorted(l1, l2))
        lists =mergedLists 
    return lists[0] 