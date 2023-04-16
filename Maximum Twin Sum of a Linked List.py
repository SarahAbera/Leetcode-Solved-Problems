# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        array = []
        length = 0
        while head:
            array.append(head.val)
            length += 1
            head = head.next

        left = 0
        right = length - 1

        maximum = 0
        while left < right:
            maximum = max(maximum, array[left] + array[right])
            left += 1
            right -= 1

        return maximum
