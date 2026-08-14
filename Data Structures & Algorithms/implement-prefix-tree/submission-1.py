
class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

                    

    def insert(self, word: str) -> None:
        current = self.root

        for char in word:

            if char not in current.children:
                current.children[char] = Node()
            current = current.children[char]
                        
    
        current.end = True


    def search(self, word: str) -> bool:

        current = self.root

        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        
        return current.end      

    def startsWith(self, prefix: str) -> bool:

        current = self.root

        for char in prefix:
            if char not in current.children:
                return False
            
            current = current.children[char]
        
        return True
        
        