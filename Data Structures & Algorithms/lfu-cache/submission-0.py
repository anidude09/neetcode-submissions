


class Node:

    def __init__(self, key: int = 0, value: int = 0 ):

        self.key = key
        self.value = value

        self.freq = 1

        self.next = None
        self.prev = None

class DLL:

    def __init__(self):
        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left

        self.size = 0 

    def addNode(self, node):

        next_node = self.left.next

        self.left.next = node
        node.prev = self.left

        node.next = next_node
        next_node.prev = node
        
        self.size += 1
    
    def removeNode(self, node):

        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

        node.prev = None
        node.next = None

        self.size -= 1



class LFUCache:

    def __init__(self, capacity: int):

        self._cap = capacity

        self._keyMap = {}
        self._freqMap = {}

        self._minFreq = 0
        self._size = 0 


    def _updateFreq(self, node):
        old_freq = node.freq

        self._freqMap[old_freq].removeNode(node)

        if (old_freq == self._minFreq and self._freqMap[old_freq].size == 0):
            self._minFreq += 1
        
        node.freq += 1

        if node.freq not in self._freqMap:
            self._freqMap[node.freq] = DLL()
        
        self._freqMap[node.freq].addNode(node)


    def get(self, key: int) -> int:

        if key not in self._keyMap:
            return -1
        
        node = self._keyMap[key]
        self._updateFreq(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:


        if self._cap == 0:
            return
        
        if key in self._keyMap:
            node = self._keyMap[key]

            node.value = value
            self._updateFreq(node)
            return
        
        if self._size == self._cap:

            min_freq_list = self._freqMap[self._minFreq]

            node_remove = min_freq_list.right.prev

            min_freq_list.removeNode(node_remove)

            del self._keyMap[node_remove.key]

            self._size -= 1
        

        newNode = Node(key, value)
        self._keyMap[key] = newNode

        if 1 not in self._freqMap:
            self._freqMap[1] = DLL()

        self._freqMap[1].addNode(newNode)

        self._minFreq = 1
        self._size += 1

        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)