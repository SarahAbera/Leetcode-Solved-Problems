# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        if not head.next:
            return [0]

        array = []
        while head:
            array.append(head.val)
            head = head.next

        monotonicDecreasingStack = []
        answer = [0] * len(array)
        for i in range(len(array)):
            while monotonicDecreasingStack and array[monotonicDecreasingStack[-1]] < array[i]:
                idx = monotonicDecreasingStack.pop()
                answer[idx] = array[i]

            monotonicDecreasingStack.append(i)

        return answer
