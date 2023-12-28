class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        count = [0] * n
        meetings.sort()
        available = [i for i in range(n)]
        hold = []
        for start, end in meetings:
            while(hold and hold[0][0] <= start):
                _, room = heappop(hold)
                heapq.heappush(available, room)

            if(available):
                room = heappop(available)
                heapq.heappush(hold, (end,room))
            
            else:
                time, room = heappop(hold)
                heapq.heappush(hold, (time + (end-start), room))
            count[room] += 1
    
        return count.index(max(count))