class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        range_ = [0] * 101
        for birth, death in logs:
            range_[birth - 1950] += 1
            range_[death - 1950] -= 1

        prefix = [0]
        for num in range_:
            prefix.append(num + prefix[-1])

        max_popu = max(prefix)
        ans = prefix.index(max_popu) + 1949
        return ans
        
        