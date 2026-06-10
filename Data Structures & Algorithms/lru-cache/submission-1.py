  

class Node:
    def __init__(self, key, value):
        self.val = value
        self.key = key
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = {}
        self.right , self.left = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def removeNode(self, node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next, nextNode.prev = nextNode, prevNode
    
    def insertNode(self, node):

        prevNode, rightNode = self.right.prev, self.right
        prevNode.next, node.prev = node, prevNode
        node.next, rightNode.prev = rightNode, node



    def get(self, key: int) -> int:

        if key in self.cache:
            self.removeNode(self.cache[key])
            self.insertNode(self.cache[key])
            return self.cache[key].val
        return -1
        
        
        

    def put(self, key: int, value: int) -> None:


        if key in self.cache:
            self.removeNode(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insertNode(self.cache[key])

        if len(self.cache) > self.cap:
            least_used = self.left.next
            del self.cache[least_used.key]
            self.removeNode(least_used)

            



        





        
