class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        def floodFill():
            visited = set()
            for row in range(len(image)):
                for col in range(len(image[0])):
                    if (row,col) not in visited and image[row][col] == image[sr][sc]:
                        component = dfs(row,col,visited)
                        if (sr,sc) in component:
                            for r , c in component:
                                image[r][c] = color
                            return image

        def inbound(new_row,new_col):
            return 0 <= new_row < len(image) and 0 <= new_col < len(image[0])

        def dfs(row,col,visited):
                stack = []
                pixels = set()
                starting_pixel = image[sr][sc]
                if image[row][col] ==  starting_pixel:
                    stack.append((row,col))
                    visited.add((row,col))
                    pixels.add((row,col))

                while stack:
                    row,col = stack.pop()
                    for i,j in directions:
                        new_row = row + i
                        new_col = col + j
                        if inbound(new_row,new_col) and (new_row,new_col) not in visited and image[new_row][new_col] == starting_pixel:
                            stack.append((new_row,new_col))
                            visited.add((new_row,new_col))
                            pixels.add((new_row,new_col))

                return pixels
                    
        return floodFill()
        
        
