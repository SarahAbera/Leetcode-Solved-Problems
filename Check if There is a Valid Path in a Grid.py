class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        parent = defaultdict()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                parent[i,j] = (i,j)


            
        directions = {(1,0) : "down", (0,1) : "right", (-1,0) : "up", (0,-1) : "left"}
       

        possible_path = {
            "right": (1,3,5),
            "left": (1,4,6),
           "up": (2,3,4),
            "down": (2,5,6)
        }
        
        street = {
            1: ("left","right"),
            2: ("up", "down"),
            3: ("left", "down"),
            4: ("down", "right"),
            5: ("left", "up"),
            6: ("up", "left")
        }

        inbound = lambda cell: 0 <= cell[0] < len(grid) and 0 <= cell[1] < len(grid[0]) 
        def find(cell):
            r,c = cell
            if parent[r,c] == (r,c):
                return (r,c)

            root = find(parent[r,c])
            parent[r,c] = root
            return root

        def union(cell1,cell2):
            rep1 = find(cell1)
            rep2 = find(cell2)

            parent[rep2] = rep1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                road = grid[i][j]
                possible_way = street[road]
                way1, way2 = possible_way
                

                for dr,dc in directions.keys():
                    way = directions[dr,dc]
                    if way != way1 and way != way2:
                        continue
                    new_r = i + dr
                    new_c = j + dc
                    if inbound((new_r, new_c)) and grid[new_r][new_c] in possible_path[way]:
                        union((i,j),(new_r,new_c))
       
        return find((0,0)) == find((len(grid)-1, len(grid[0]) - 1))
