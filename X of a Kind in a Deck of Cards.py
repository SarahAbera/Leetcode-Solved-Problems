class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False

        hashMap = defaultdict(int)
        for num in deck:
            hashMap[num] += 1

        count = []
        for key,val in hashMap.items():
            count.append(val)

        greatestCommonDivisor = gcd(*count)
        if greatestCommonDivisor > 1:
            return True
        return False
