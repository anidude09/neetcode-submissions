
class Node:

    def __init__(self):

        self.next = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:

        cur = self.root

        for char in word:
            if char not in cur.next:
                cur.next[char] = Node()
            cur = cur.next[char]
        
        cur.end = True
        

    def search(self, word: str) -> bool:


        def dfs(node, index):
            if index == len(word):
                return node.end

            
            char = word[index]

            if char == ".":
                for child in node.next.values():
                    if dfs(child, index + 1):
                        return True
                return False
            else:
                if char in node.next:
                    if dfs(node.next[char], index + 1):
                        return True
                return False
            
        return dfs(self.root, 0)









        
