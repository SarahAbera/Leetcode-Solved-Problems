class Solution:
    def findComplement(self, num: int) -> int:
        val = num
        count = 0
        while num != 0:
            num >>= 1
            count += 1
        return val ^ (pow(2,count)-1)
