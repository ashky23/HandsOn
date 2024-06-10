class Node:
    key = None
    val = None
    prev = None
    inext = None
    
    def __init__(self, key = None, val = None,  prev = None, inext = None) -> None:
        self.key = key
        self.val = val
        self.prev = prev
        self.inext = inext
        