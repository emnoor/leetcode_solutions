class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        i = 0
        total_cost = 0
        while i < n:
            mx = 0
            sm = 0
            for j in range(i, n):
                if colors[j] != colors[i]:
                    i = j
                    break
                sm += neededTime[j]
                if neededTime[j] > mx:
                    mx = neededTime[j]
            else:
                i = n
            total_cost += sm - mx
        return total_cost