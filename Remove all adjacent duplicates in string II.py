class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for char in s:
            if stack:
                count, w = stack[-1]
                if w == char:
                    stack.append((count + 1, char))
                else:
                    stack.append((1,char))
            else:
                stack.append((1,char))
            count = stack[-1][0]
            while stack and count == k:
                while count:
                    stack.pop()
                    count -= 1

        ans = ""
        for c,w in stack:
            ans += w
        return ans
            
