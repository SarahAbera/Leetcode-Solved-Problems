class Solution:
    def maxLength(self, arr: List[str]) -> int:

        maximum = 0
        def backtrack(start,chars):
            nonlocal maximum
            string = "".join(chars)
            if len(string) == len(set(string)):
                maximum = max(maximum, len(string))

            for i in range(start,len(arr)):
                chars.append(arr[i])
                backtrack(i+1, chars)
                chars.pop()

        backtrack(0,[])

        return maximum
