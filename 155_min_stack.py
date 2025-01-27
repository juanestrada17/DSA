class MinStack:

    def __init__(self):
        self.stack = []
        self.min_els = []
        
    def push(self, val: int) -> None:
        self.stack = self.stack + [val]
                        
        if(not self.min_els or val < self.min_els[-1]):
            self.min_els = self.min_els + [val]
        
    def pop(self) -> None:
        deleted_value = self.stack.pop()
        cur_lowest_element = len(self.min_els) - 1

    
        if(self.min_els and deleted_value == self.min_els[cur_lowest_element]):
            self.min_els.pop()

        
    def top(self) -> int:
        if(self.stack):
            last_element = len(self.stack) - 1
        return self.stack[last_element] if self.stack else []

    def getMin(self) -> int:
        cur_lowest_element = len(self.min_els) - 1
        return self.min_els[cur_lowest_element] if self.min_els else []


# stack = [395,276, 29, \-428\ , -108, \-251, \-439, \370]
# second_Stack = [395,276, 29, \-428\ , -108, \-251, \-439, \370]

# 395, 276, 29, -108, 

obj = MinStack()
obj.push(395) # min 395 
print(obj.getMin())
# "top",
print(obj.getMin())
obj.push(276) #  min 276
obj.push(29) #min 29
print(obj.getMin())
obj.push(-482) # min -482
print(obj.getMin())
obj.pop()
obj.push(-108) # min -108 
obj.push(-251) # min -251
print(obj.getMin()) # min- 251 
obj.push(-439) # min -439
# "top",
obj.push(370) # min -439 
obj.pop() # min -439
obj.pop() # min -251
print(obj.getMin()) # min -251 
obj.pop() # min -108
print(obj.getMin()) #min -108
print(obj.getMin()) #min -108
obj.pop() # min 29
print(obj.getMin())
obj.push(-158) # 2 / inf
obj.push(82) # 2 / inf
obj.pop()
obj.push(-176) # 2 / inf
print(obj.getMin())
print(obj.getMin())
obj.push(-90) # 2 / inf
print(obj.getMin())

