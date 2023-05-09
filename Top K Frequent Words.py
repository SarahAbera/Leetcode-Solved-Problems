class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency_of_each_word = Counter(words)
        with_same_frequency = defaultdict(list)
        
        for key,val in frequency_of_each_word.items():
            with_same_frequency[-val].append(key)

        frequency_arr = []
        for key,val in with_same_frequency.items():
            frequency_arr.append((key,sorted(set(val))))

        heapify(frequency_arr)
        
        answer = []
        length = k
        while k > 0:
            val, words = heappop(frequency_arr)
            for word in words:
                if  len(answer) < length:
                    answer.append(word)
            k -= len(words)

        return answer
