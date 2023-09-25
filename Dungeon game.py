class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        target = (len(dungeon)-1, len(dungeon[0])-1)
        inbound = lambda x,y : 0 <= x < len(dungeon) and 0 <= y < len(dungeon[0])
        
        def dp(r,c):
            if (r,c) == target:
                if dungeon[r][c] <= 0:
                    return 1 - (dungeon[r][c])
                return 1

            go_down = dp(r+1,c) if inbound(r+1,c) else inf
            go_right = dp(r, c+1) if inbound(r, c+1) else inf

            fast_path = min(go_right, go_down) - dungeon[r][c]
            return fast_path if fast_path > 0 else 1
            
        val = dp(0,0)   
        return val if val != inf else 1
