class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = Counter(s1)
        
        countS2 = defaultdict(int)

        left = 0
        for right in range(len(s2)):
            countS2[s2[right]] += 1

            if countS2 == countS1:
                return True

            if (right - left + 1) == len(s1):
                countS2[s2[left]] -= 1
                if countS2[s2[left]] == 0:
                    del countS2[s2[left]]
                left += 1

            

        return False

            
