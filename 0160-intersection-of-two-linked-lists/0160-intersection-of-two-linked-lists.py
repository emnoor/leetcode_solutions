# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pa = headA
        pb = headB
        
        na = 1
        while pa.next:
            na += 1
            pa = pa.next
        
        nb = 1
        while pb.next:
            nb += 1
            pb = pb.next
        
        # if pa is not pb:
        #     return None
        
        pa = headA
        for _ in range(na - nb):
            pa = pa.next

        pb = headB
        for _ in range(nb - na):
            pb = pb.next
        
        for _ in range(min(na, nb)):
            if pa is pb:
                return pa
            pa = pa.next
            pb = pb.next

        return None