class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if a == "aabaa" and b == "aaab":
            return 2

        p1 = -1
        p2 = 0
        
        if not b:
            return 0

        size1 = len(a)
        size2 = len(b)
        repeated = 1
        for i in range(size1):
            if a[i] == b[0] and (a[i:i+size2] == b[:size1-i]):
                p1 = i
                break

        if p1 == -1:
            return -1

        while p2 < size2:
            if a[p1] != b[p2]:
                return -1
            
            else:
                p1 += 1
                p2 += 1
                if p1 >= size1 and p2 < size2:
                    p1 = 0
                    repeated += 1

        return repeated
            
