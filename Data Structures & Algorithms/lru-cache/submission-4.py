
class Node:
    def __init__(self, key: int, value:int, next , prev):
        self.key = key
        self.value = value

        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0, 0, None, None)
        self.right = Node(0,0, None, None)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return - 1
        
        node = self.cache[key]
        self.removeNode(node)
        self.addNode(node)
        return node.value

    def removeNode(self, node: Node):
        nxt = node.next
        prv = node.prev
        prv.next = nxt
        nxt.prev = prv


    
    def addNode(self, node: Node):
        prv = self.right.prev
        prv.next = node
        node.prev = prv
        node.next = self.right
        self.right.prev = node
        
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            oldNode = self.cache[key]
            self.removeNode(oldNode)
            oldNode.value = value
            self.addNode(oldNode)
        else:
            self.cache[key] = Node(key, value, None, None)
            newNode = self.cache[key]
            self.addNode(newNode)

        if len(self.cache) > self.cap:
            LRnode = self.left.next
            self.removeNode(LRnode)
            del self.cache[LRnode.key]
        




        
