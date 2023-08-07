class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(s):
            nei = []
            for i, c in enumerate(s):
                for d in [1, -1]:
                    nei.append(s[:i] + str((int(c)+d) % 10) + s[i+1:])
            return nei    
        deadends = set(deadends)
        if '0000' in deadends: return -1
        if '0000' == target: return 0
        q = deque(['0000'])
        dist = {'0000': 0}
        while q:
            num = q.popleft()
            d = dist[num] + 1
            for nei in neighbors(num):
                if nei not in dist and nei not in deadends:
                    if nei == target:
                        return  d
                    q.append(nei)
                    dist[nei] = d
        return -1
