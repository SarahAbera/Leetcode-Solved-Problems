class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapify(piles)

        while k:
            stones = -heappop(piles)
            removed = stones // 2
            stones -= removed
            heappush(piles, -stones)

            k -= 1

        return -sum(piles)
