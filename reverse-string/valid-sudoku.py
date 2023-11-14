class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                element = board[i][j]

                if element == ".":
                    continue
                else:
                    if element in row[i] or element in col[j] or element in box[i//3][j//3]:
                        return False
                row[i].add(element)
                col[j].add(element)
                box[i//3][j//3].add(element)
        return True