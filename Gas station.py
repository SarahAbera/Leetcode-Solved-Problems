class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        net_gas = [gas[i] - cost[i] for i in range(len(cost))]
        if sum(net_gas) < 0:
            return -1

        tank = 0
        start = 0
        for i, gas in enumerate(net_gas):
            tank += gas
            if tank < 0:
                tank = 0
                start = i + 1
            
        return start
