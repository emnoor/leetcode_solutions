# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def jump(node):
    if not node:
        return node
    return node.next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle = jump(head)
        here = jump(jump(head))
        
        while turtle and here and turtle != here:
            turtle = jump(turtle)
            here = jump(jump(here))
            
        return turtle and here and turtle == here