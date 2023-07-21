class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words_ = []
        for word in words:
            count = Counter(word)
            words_.append(count)
        
        for i in range(len(words) - 1):
            for j in range(i+1, len(words)):
                word1 = words_[i]
                word2 = words_[j]
                for key,val in word1:
                    if key in word2:
