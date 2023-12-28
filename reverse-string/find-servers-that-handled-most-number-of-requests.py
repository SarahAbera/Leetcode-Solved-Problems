class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        
        from sortedcontainers import SortedList
        avail = SortedList()        # like AVL Tree
        
        for i in range(k):  #Initially all servers are available
            avail.add(i)
        
        h = []  #(endtime, server index)  (busy servers) (heap to record the busy servers)
        
        count = [0]*k 
        
        for i in range(len(arrival)):
            s = arrival[i]
            e = arrival[i]+load[i]
            while h and h[0][0]<=s:       # remove all the servers from heap that becomes free now
                _, j = heappop(h)
                avail.add(j)
            
            if len(h)==k:
                continue
                
            si = avail.bisect_left(i%k)     # get  server index
            if si==len(avail):
                ser = avail[0]
            else:
                ser = avail[si]         
                
            # assign request to this server
            avail.remove(ser)               
            count[ser]+=1
            heappush(h, (e, ser))
        
        maxReq = max(count)
        ans = []
        for i in range(len(count)):
            if count[i]==maxReq:
                ans.append(i)
        return ans
    
            