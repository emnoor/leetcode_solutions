# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        level = [root]
        reverse = True

        while level:
            reverse = not reverse
            new_level = []
            level_vals = []
            for node in level:
                if node:
                    level_vals.append(node.val)
                    new_level.append(node.left)
                    new_level.append(node.right)
            
            if reverse:
                level_vals = level_vals[::-1]
            
            if level_vals:
                result.append(level_vals)

            level = new_level
        
        return result
