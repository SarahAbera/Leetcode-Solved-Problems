# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode()
        greater = dummy
        dummy2 = ListNode()
        smaller = dummy2

        while head:
            if head.val < x:
                smaller.next = head
                smaller = smaller.next
                  
            else:
                greater.next = head
                greater = greater.next

            head = head.next
    
        greater.next = None

        dummy = dummy.next
        smaller.next = dummy
        return dummy2.next
