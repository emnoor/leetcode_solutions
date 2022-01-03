# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def flatten(node, lst):
            if node is None:
                return
            
            lst.append(node.val)
            flatten(node.left, lst)
            flatten(node.right, lst)

        lst = []
        flatten(root, lst)
        lst.sort()
        return lst[k - 1]