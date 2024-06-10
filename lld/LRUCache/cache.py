from dllNode import Node
class LRUCache:
    dllHead = None
    dllTail = None
    dllHashMap = None
    cacheSize = 0
    cacheCapacity = 0
    
    def __init__(self, cacheCapacity) -> None:
        self.cacheCapacity = cacheCapacity
        self.dllHashMap = dict()
    
    def get(self, key: str) -> any:
        print(self.dllHashMap)
        key_node = self.dllHashMap.get(key)
        if key_node:
            return key_node.val
        else:
            return None

    def set(self, key: str, val: any) -> bool:
        # check if key exists in hash
        # if exists move from that posiition to end /tail
        # if doesn't exist add one node at tail - inc size if size > cap, remove head
        
        if key in self.dllHashMap:
            key_node = self.dllHashMap.get(key)
            if self.cacheSize == 1: # head and tail is same - no rebalance required 
                return True
            key_node.val = val
            prev_node = key_node.prev
            inext_node = key_node.inext
            if self.dllHead == key_node:
                self.dllHead = inext_node
                inext_node.prev = None
                key_node.prev = self.dllTail
                key_node.inext = None
                self.dllTail = key_node
                
            elif self.dllTail == key_node:
                return True
            
            else: # More than 2 node 
                prev_node.inext = inext_node
                inext_node.prev = prev_node
                key_node.prev = self.dllTail
                key_node.inext = None
                self.dllTail = key_node
     
        else:
            new_key_node = Node(key=key, val=val, prev=self.dllTail, inext=None)
            self.dllHashMap[key] = new_key_node
            if self.dllTail:
                self.dllTail.inext = new_key_node
            self.dllTail = new_key_node
            self.cacheSize+=1
            if self.cacheSize > self.cacheCapacity: # delete head
                del self.dllHashMap[self.dllHead.key]
                self.dllHead = self.dllHead.inext
                self.dllHead.prev = None
                
            if self.cacheSize == 1:
                self.dllHead = new_key_node
                
            print(self.dllHashMap)
            
        
