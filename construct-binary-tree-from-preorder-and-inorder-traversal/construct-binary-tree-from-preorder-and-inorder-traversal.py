# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(val=preorder[0])
        node_map = {preorder[0]: root}
        node = root
        left = True
        
        for i in inorder:
            if (tmp := node_map.get(i)):
                node = tmp
                left = False
                continue
            
            for p in preorder:
                if node_map.get(p):
                    continue
                
                new_node = TreeNode(val=p)
                if left:
                    node.left = new_node
                else:
                    node.right = new_node
                    left = True
                    
                node = new_node
                node_map[p] = new_node

                if p == i:
                    break
            
            left = False
        
        return root
