# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        
        new_head = head.next
        head.next, new_head.next = new_head.next, head
        
        prev = new_head.next
        a = prev.next if prev else None
        b = a.next if a else None
        
        while prev and a and b:
            prev.next, a.next, b.next = b, b.next, a
            
            prev = b.next
            a = prev.next if prev else None
            b = a.next if a else None
        
        return new_head