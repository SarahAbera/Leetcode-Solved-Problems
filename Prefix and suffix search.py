class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        t = self.trie
        for letter in word:
            if letter not in t:
                t[letter] = {}
            t = t[letter]
        t['#'] = '#' 

    def search(self, word: str) -> bool:
        t = self.trie
        for letter in word:
            if letter not in t: return False
            t = t[letter]
        if '#' in t: return True
        else: return False

    def startsWith(self, prefix: str) -> bool:
        t = self.trie
        for letter in prefix:
            if letter not in t: return (False, None)
            t = t[letter]
        return (True, t)

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.indexes = dict()
        for i in range(len(words)):
            self.trie.insert(words[i])
            self.indexes[words[i]] = i

    def get_words_by_pref(self, pref, t, words):
        if '#' in t:
            words.append(pref)
        for letter in t:
            if letter != '#':
                t_next = t[letter]
                self.get_words_by_pref(pref+letter, t_next, words)

        

    def f(self, pref: str, suff: str) -> int:
        starts_with, t = self.trie.startsWith(pref)
        if starts_with:
            words = []
            self.get_words_by_pref(pref, t, words)
        else:
            return -1

        if not words: return -1
        idx = -1
        for word in words:
            if len(suff) <= len(word) and suff == word[-len(suff):]:
                idx = max(idx, self.indexes[word])
        
        return idx
