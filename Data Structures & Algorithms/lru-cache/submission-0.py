#node for last to first used keys
class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None

#dictionary map key to value
class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache = {}

        self.left=Node(0,0)
        self.right=Node(0,0)

        # left-node <-> right-node
        self.left.next=self.right
        self.right.prev=self.left
    
    #make functions: insert and remove
    def remove(self,node):
        prev_of_node=node.prev
        next_of_node=node.next
        prev_of_node.next=next_of_node
        next_of_node.prev=prev_of_node

    def insert(self,node):

        self.right.prev.next=node
        node.prev=self.right.prev
        node.next=self.right
        self.right.prev=node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        #if key exist remove then add new key,value pair
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])
    
        #check length and remove LRU if needed
        if len(self.cache) > self.cap:
            LRU=self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]
            


        
