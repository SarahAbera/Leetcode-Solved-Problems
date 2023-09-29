class Trie:
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self,word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
            if len(cur.words) < 3:
                cur.words.append(word)
                
    
    def find_word_by_prefix(self,prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return ""
            curr = curr.children[char]
        return curr.words

class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []
        

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()

        for product in products:
            trie.insert(product)

        result = []
        for i in range(len(searchWord)):
            ans = trie.find_word_by_prefix(searchWord[:i+1])
            result.append(ans)
        return result
            
