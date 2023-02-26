class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total = sum(gas[i] - cost[i] for i in range(n))
        if (total < 0):
            return -1

        tank = 0
        start = 0
        for i in range(n):
            tank += gas[i] - cost[i]

            if (tank < 0):
                start = i+1
                tank = 0

        return start