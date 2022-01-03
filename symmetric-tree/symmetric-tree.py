get_left = lambda node: node.left if node else None
get_right = lambda node: node.right if node else None
get_val = lambda node: node.val if node else None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        level = [root]
        
        while True:
            if all(x is None for x in level):
                return True
            
            if [get_val(x) for x in level] != [get_val(x) for x in reversed(level)]:
                return False
            
            
            level = [f(x) for x in level for f in (get_left, get_right)]
        
        return True