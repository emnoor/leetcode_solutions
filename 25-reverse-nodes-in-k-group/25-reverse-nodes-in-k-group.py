from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1 or not head or not head.next:
            return head
        
        stack = []
        new_head = None
        prev_node = None
        
        while head:
            for _ in range(k):
                stack.append(head)
                head = head.next
                if head is None:
                    break
            
            if len(stack) < k:
                if new_head is None:
                    new_head = stack[0]
                elif prev_node is not None:
                    prev_node.next = stack[0]
            else:
                while stack:
                    node = stack.pop()
                    node.next = None

                    if new_head is None:
                        new_head = node

                    if prev_node is not None:
                        prev_node.next = node

                    prev_node = node
        
        return new_head
