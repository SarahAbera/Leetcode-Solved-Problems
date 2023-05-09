class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        array = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                array.append(matrix[r][c])
        array.sort()
        return array[k-1]
