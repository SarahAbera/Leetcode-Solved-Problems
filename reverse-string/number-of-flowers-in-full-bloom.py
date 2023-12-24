class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        hashmap = defaultdict(int)
        for start, end in flowers:
            hashmap[start] += 1
            hashmap[end+1] -= 1

        sortedHashmap = sorted(hashmap.items())
        time = [sortedHashmap[i][0] for i in range(len(sortedHashmap))]
        bloomedFlower = [sortedHashmap[i][1] for i in range(len(sortedHashmap))]

        prefix = [0]
        for num in bloomedFlower:
            prefix.append(prefix[-1] + num)
        prefix = prefix[1:]

        ans = []
        for num in people:
            idx = bisect_right(time,num)
            ans.append(prefix[idx-1])
        
        return ans


        