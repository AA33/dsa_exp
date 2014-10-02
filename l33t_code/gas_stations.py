class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas_station, cost):
        if len(gas_station) == 0 or len(cost) == 0 or len(gas_station) != len(cost):
            return -1
        diffs = []
        for i in range(len(gas_station)):
            diffs[i] = gas_station[i] - cost[i]
        for i
