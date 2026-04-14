class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])

        arrow=0
        end=float('-inf')

        for p in points:
            if p[0]>end:
                arrow+=1
                end=p[1]
        return arrow