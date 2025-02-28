class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        
        # These are dummy nodes 
        self.oldest = Node(0, 0)
        self.latest = Node(0, 0)
        # example oldest -> [1,1] -> [2,2] -> latest
        self.oldest.next = self.latest
        self.latest.prev = self.oldest
        
    def get(self, key: int) -> int: 
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1 
    
    def remove(self, node): 
        prev, next = node.prev, node.next
        # Skip node
        prev.next = next
        next.prev = prev
        
    def insert(self, node):
        prev, next = self.latest.prev, self.latest
        prev.next = next.prev = node
        node.next = next
        node.prev = prev
    
    def put(self, key: int, value: int) -> None: 
        if key in self.cache:
            # We don't remove from the dict because we haven't reached the cap
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            # lru is oldest.next, remember that it's a dummy node.
            lru = self.oldest.next
            self.remove(lru)
            # We remove from the cache also
            del self.cache[lru.key]