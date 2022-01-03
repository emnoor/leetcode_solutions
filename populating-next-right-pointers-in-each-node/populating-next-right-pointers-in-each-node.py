"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        level = [root]
        
        while True:
            new_level = []
            
            for node in level:
                if not node.left:
                    break
                    
                new_level.append(node.left)
                new_level.append(node.right)
            
            if not new_level:
                break
            
            for i in range(len(new_level) - 1):
                new_level[i].next = new_level[i + 1]
            
            level = new_level
        
        return root