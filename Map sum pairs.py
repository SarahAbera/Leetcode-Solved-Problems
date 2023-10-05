class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefixCount = 0
        
        
class MapSum:  

    def __init__(self):
        self.root = TrieNode()
        self.dic = {}

    def insert(self, key: str, val: int) -> None: 
        delta = val
        if key in self.dic: 
            delta = val - self.dic[key]
        self.dic[key] = val
        cur = self.root
        for c in key:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.prefixCount += delta

    def sum(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        return cur.prefixCount

