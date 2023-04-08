class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        count = []
        for key,val in frequency.items():
            count.append((val,key))
        
        
        count.sort(reverse = True)
        ans = []
        for i in range(k):
            ans.append(count[i][1])

        return ans
