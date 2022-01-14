# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        lst.sort()
        
        head, prev = None, None
        for x in lst:
            node = ListNode(val=x)
            if not head:
                head = node
            if prev:
                prev.next = node
            prev = node
        
        return head