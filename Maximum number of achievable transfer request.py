class Solution:
    def __init__(self):
        self.ans = 0
        self.requests = []

    def maximumRequests(self, n, requests):
        self.requests = requests
        transfers = [0] * n
        self.backTrack(0, 0, transfers)
        return self.ans

    def backTrack(self, index, count, transfers):
        if index == len(self.requests):
            if all(i == 0 for i in transfers):
                self.ans = max(self.ans, count)
            return
        
        transfers[self.requests[index][0]] -= 1
        transfers[self.requests[index][1]] += 1
        self.backTrack(index + 1, count + 1, transfers)
        
        transfers[self.requests[index][0]] += 1
        transfers[self.requests[index][1]] -= 1
        self.backTrack(index + 1, count, transfers)

        
