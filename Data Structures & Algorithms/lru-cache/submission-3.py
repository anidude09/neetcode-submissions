class Node:
    def __init__(self, key, value):
        self.val = value
        self.key = key
        self.next, self.prev = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left   

    def removeNode(self, node):
        l, r = node.prev, node.next
        l.next, r.prev = r, l 

    def insertNode(self, node):
        l, r = self.right.prev, self.right
        l.next = r.prev = node
        node.prev, node.next = l, r


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
            least = self.left.next
            del self.cache[least.key]
            self.removeNode(least)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)