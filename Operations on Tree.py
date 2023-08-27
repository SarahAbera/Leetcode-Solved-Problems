class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locked = {i:(False,-1) for i in range(len(parent))}
        self.graph = defaultdict(list)
        for i in range(len(parent)):
            self.graph[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        if not self.locked[num][0]:
            self.locked[num] = (True, user)
            return True
        else: return False
        
    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num][0] and self.locked[num][1] == user:
            self.locked[num] = (False, -1)
            return True
        else: return False
        
    def upgrade(self, num: int, user: int) -> bool:
        if self.locked[num][0]:
            return False
        i = num
        while i != -1:
            if self.locked[i][0]:
                return False
            i = self.parent[i]

        count = 0   
        def dfs(node):
            nonlocal count
            if self.locked[node][0]:
                count += 1
                self.locked[node] = (False,-1)
            if not self.graph[node]:
                return
            for ngh in self.graph[node]:
                dfs(ngh)
        dfs(num)
        if count > 0:
            self.locked[num] = (True,user)
            return True

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
