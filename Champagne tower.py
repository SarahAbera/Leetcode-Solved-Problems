class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        print(query_row,query_glass)
        glasses = [[0.0] * (i + 1) for i in range(query_row + 2)]
        glasses[0][0] = poured
        for i in range(query_row + 1):
            for j in range(len(glasses[i])):
                if glasses[i][j] >= 1.0:
                    overfill = glasses[i][j] - 1.0
                    glasses[i][j] = 1.0
                    glasses[i+1][j] += overfill / 2
                    glasses[i+1][j+1] += overfill / 2

        return glasses[query_row][query_glass]
