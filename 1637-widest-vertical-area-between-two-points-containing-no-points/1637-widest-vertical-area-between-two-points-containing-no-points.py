class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        
        d = 0
        for i in range(len(points) - 1):
            nd = points[i+1][0] - points[i][0]
            if nd > d:
                d = nd
        return d