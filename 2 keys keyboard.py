class Solution:
    def minSteps(self, n: int) -> int:
        curr = 1
        clipboard = 0
        steps = 0

        while curr < n:
            if n % curr == 0:
                clipboard = curr
                steps += 1

            curr += clipboard
            steps += 1

        return steps
        
