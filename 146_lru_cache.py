# Each node has the key and the value
class Node:
    def __init__(self, key=None, value=None, next=None, prev=None):
        self.key = key
        self.value = value 
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.keyVals = {}
    
    # Retrieve all elements in head
    def print_all(self):
        current = self.head
        while current: 
            print(f"{current.key}:{current.value}")
            current = current.next

    # Insert start method 
    def insert_start(self, key, value):
        new_node = Node(key, value)
        
        # Stores reference of it to the dict
        self.keyVals[key] = new_node
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        return self.head
    
    def delete_node(self, key):
        del_node = self.keyVals[key]
        # If the del_node is the head
        if del_node == self.head:
            self.head = del_node.next
    
        if del_node.prev: 
            del_node.prev.next = del_node.next
        if del_node.next:
            del_node.next.prev = del_node.prev

        # Get a hold of its value
        value = del_node.value

        # Delete it from the list 
        del del_node
        # Delete it from the dictionary 
        del self.keyVals[key]
        return value

    # This deletes the tail 
    def delete_last_node(self):
        if not self.tail:
            return
        del self.keyVals[self.tail.key]
        # If head and tail are the same we just set them to none
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            # We set the tail to the prev element 
            self.tail = self.tail.prev
            # We set the new tail's next to None 
            self.tail.next = None
    
    def set_most_recent(self, key):
        # Handles case when the tail is being set as the recent, we need to re arrange recents
        if self.keyVals[key] == self.tail:
            self.tail = self.tail.prev 
        # Delete it at its position and from dict
        del_value = self.delete_node(key)
        # Insert at the start and add again to dictionary 
        self.head = self.insert_start(key, del_value)
        
    # Retrieves the value if it exists, else, returns -1 
    # Changes the position of latest to the new key 
    def get(self, key: int) -> int:
        # If the key exists we return its value
        if key in self.keyVals: 
            self.set_most_recent(key)
            return self.keyVals[key].value
        else: 
            return -1 
        
    # 1. Adds new key - values to the LRU IF they don't exist 
    # 2. If the len of the keyVals exceeds the capacity AND new key. We delete last and insert to start 
    #     else : we add new key and value
    def put(self, key: int, value: int) -> None:
        if key in self.keyVals: 
            # Set it as the most recent
            self.set_most_recent(key)
            # update its value
            self.keyVals[key].value = value
        else: 
            if len(self.keyVals) < self.capacity:
                self.head = self.insert_start(key, value)
            else: 
                self.delete_last_node()
                self.head = self.insert_start(key, value)
    
    def print_tail(self):
        print(self.tail.key)
        
        
obj = LRUCache(capacity=1)
obj.get(6)
obj.get(8)
obj.put(12,1)
obj.get(2)
obj.put(15,11)
obj.print_all()
