from collections import deque
nums = [1,3,-1,-3,5,3,6,7]
k = 3
nums = [7,2,4]
k = 2
# Neetcode decreasing monotonic queue approach 
def calc_max(nums, k):
    output = []
    max_els = deque()
    l = r = 0
    
    # r is in bounds
    while r < len(nums):
        # While the top(end) of the queue is less than
        # the new element. 
        # WHILE smaller values exist in the queue
        while max_els and nums[max_els[-1]] < nums[r]:
            max_els.pop()
        
        # We store the indices since it's easy to retrieve them
        max_els.append(r)
        
        # If the left index is higher than the index of the max element
        # It means the previous element and its index is no longer in the window
        if l > max_els[0]:
            max_els.popleft()
            
        if r - l + 1 >= k:
            output.append(nums[max_els[0]])
            l += 1
        r += 1
    return output 
        
# print(calc_max(nums, k))


def find_max(nums, k):
    # Append each max to it
    res = []
    # data structure to maining max element at top, in decreasing order
    monotonic_queue = deque()
    
    left = 0 
    for right in range(len(nums)):
        
        # But before appending, we need to maintain the queue in decreasing order
        while monotonic_queue and nums[monotonic_queue[-1]] < nums[right]:
            # We pop all elements that are less that the new right elements, making sure the new highest will be at the start of the queue
            monotonic_queue.pop()
        
        
        # We need to append right to the queue 
        monotonic_queue.append(right)

        
        if left > monotonic_queue[0]:
            # We check if the index of the greatest is smaller than the current left index. If it is we eliminate it. 
            monotonic_queue.popleft()
        
        
        # We need to check if the current window size is k, so we calculate the distance 
        if right - left + 1 >= k:
            # We add the greatest element, which is in this case the first element of the queue
            # Since we are working with the indeces, we have to access the element when we append
            res.append(nums[monotonic_queue[0]])
            # We increase left, because we reached k window size
            left += 1
        # But, what do we do when the max element in the que is no longer in the window?
    return res
# print(find_max(nums, k))


def search_max(nums, k):
    # array that contains response
    res = []
    # decreasing queue to get a hold of the max element at every time 
    monotonic_queue = deque()
    left = 0
    for right in range(len(nums)):
        
        # Before we append it we need to make sure that the leftmost element is not less than the current right 
        while monotonic_queue and nums[monotonic_queue[-1]] < nums[right]:
            # Remove all elements that are less that right 
            monotonic_queue.pop()
        
        # We append the right element to the queue
        monotonic_queue.append(right)
        
        # We need to check if the current window size is equals or more than k
        if right - left + 1 >= k:
            # We store the current max to the response 
            res.append(nums[monotonic_queue[0]])
            # this is when we move the window
            left += 1
            
        # We need to check if the current max is no longer in the window
        if left > monotonic_queue[0]:
            monotonic_queue.popleft()
    return res 

print(search_max(nums, k))






    
    
    



