class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.children = defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name) 

    def getInheritanceOrder(self) -> List[str]:
        visited = set(self.kingName)
        def dfs(king,successors):
            if not self.children[king]:
                return successors

            if king not in visited:
                visited.add(king)
                for child in self.children[king]:
                    if child not in self.dead:
                        successors.append(child)
                    dfs(child,successors)
            return successors   

        successor = [self.kingName] if self.kingName not in self.dead else []   
        return dfs(self.kingName,successor)
                
# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
