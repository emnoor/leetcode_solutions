# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        
        old_head = head
        
        odd_head = odd = head
        head = head.next
        even_head = even = head
        head = head.next
        i = 3
        
        while head:
            if i % 2 == 0:
                even.next = head
                even = head
            else:
                odd.next = head
                odd = head
            
            head = head.next
            i += 1
        
        odd.next = even_head
        even.next = None
        
        return old_head
            