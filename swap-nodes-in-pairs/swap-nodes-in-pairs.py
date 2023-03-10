# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:       
        cur = head  
        if not(cur) or not(cur.next):
            return cur
        
        _next = cur.next
        temp = _next.next
        _next.next = cur
        cur.next = self.swapPairs(temp)
        return _next