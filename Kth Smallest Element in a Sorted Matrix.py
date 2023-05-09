class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        array = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                array.append(matrix[r][c])
        array.sort()
        return array[k-1]

 
# heap solution
    
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        array = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                array.append(matrix[r][c])
        
        heapify(array)
        while k > 1:
            heappop(array)
            k -= 1

        return heappop(array)
