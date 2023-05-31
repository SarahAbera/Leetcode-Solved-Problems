class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        ways = [[0]*n for _ in range(m)]
        
        for i in range(n):
            ways[m-1][i] = 1

        for j in range(m):
            ways[j][n-1] = 1

        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                ways[i][j] = ways[i+1][j] + ways[i][j+1]
        
        return ways[0][0]
