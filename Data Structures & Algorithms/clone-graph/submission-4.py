"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:


        graph = {}

        def clone(node):
            if node in graph:
                return graph[node]
            
            graph[node] = copy = Node(node.val)

            for child in node.neighbors:
                copy.neighbors.append(clone(child))

            return copy
        
        return clone(node) if node else None



        


        