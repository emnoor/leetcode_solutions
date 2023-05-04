# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_nodes = [root]
        q_nodes = [root]

        def dfs(start, target, lst):
            if start is target:
                return True

            if not start:
                return False

            lst.append(start.left)
            left = dfs(start.left, target, lst)
            if left:
                return True

            lst.pop()

            lst.append(start.right)
            right = dfs(start.right, target, lst)
            if right:
                return True

            lst.pop()
            return False

        dfs(root, p, p_nodes)
        dfs(root, q, q_nodes)

        i = 0
        while True:
            if i >= len(p_nodes) or i >= len(q_nodes) or p_nodes[i] is not q_nodes[i]:
                break
            i += 1

        return p_nodes[i - 1]