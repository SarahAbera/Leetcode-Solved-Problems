class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        #self.nums = [-num for num in self.nums]
        heapify(self.nums)
        n = len(self.nums)
        
        while len(self.nums) > k:
            heappop(self.nums)
            


    def add(self, val: int) -> int:
        heappush(self.nums,val)
        if len(self.nums) > self.k:
            heappop(self.nums)
        return self.nums[0]
        
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
