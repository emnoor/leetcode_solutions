# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        if not root:
            return "()"
        
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return f"({root.val}{left}{right})"

    def deserialize(self, data: str) -> TreeNode:
        if not data or data == "()":
            return None
        
        end = data[1:].find('(') + 1
        val = int(data[1:end])
        
        i = end
        j = i + 1
        lp = 1
        rp = 0
        while lp != rp:
            if data[j] == '(':
                lp += 1
            elif data[j] == ')':
                rp += 1
            j += 1
            
        left = self.deserialize(data[i:j])
        
        i = j
        j = i + 1
        lp = 1
        rp = 0
        while lp != rp:
            if data[j] == '(':
                lp += 1
            elif data[j] == ')':
                rp += 1
            j += 1
        
        right = self.deserialize(data[i:j])
        
        node = TreeNode(val)
        node.left = left
        node.right = right
        return node
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))