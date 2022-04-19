# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        if not traversal:
            return None

        number_of_digits = traversal.find('-')
        if number_of_digits > 0:
            number = traversal[:number_of_digits]
            traversal = traversal[number_of_digits:]
        else:
            number = traversal
            traversal = ""

        root = TreeNode(number)
        stack = [(root, 0)]  # stack of (node, node_depth)

        while traversal:
            dashes = 0
            for c in traversal:
                if c != "-":
                    break
                dashes += 1

            node, node_depth = stack[-1]
            if dashes != node_depth + 1:
                stack.pop()
                continue

            number_of_digits = traversal[dashes:].find('-')
            if number_of_digits > 0:
                number = traversal[dashes:dashes+number_of_digits]
                traversal = traversal[dashes+number_of_digits:]
            else:
                number = traversal[dashes:]
                traversal = ""

            new_node = TreeNode(number)

            if not node.left:
                node.left = new_node
            else:
                node.right = new_node

            stack.append((new_node, dashes))

        return root