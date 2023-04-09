# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        if not head.next or k == 0:
            return head

        curr = head
        lengthOfLinkedList = 0

        while curr and curr.next:
            lengthOfLinkedList += 1
            curr = curr.next
        lengthOfLinkedList += 1

        k = k % lengthOfLinkedList
        rotates = abs(lengthOfLinkedList - k)
        if rotates == lengthOfLinkedList:
            return head
        Head = head
        while rotates > 1:
            Head = Head.next
            rotates -= 1
        new_head = Head.next
        Head.next = None
        curr.next = head

        return new_head
