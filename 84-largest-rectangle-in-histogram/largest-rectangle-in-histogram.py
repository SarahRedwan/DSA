class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_a=0
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i]<heights[stack[-1]]:
                h=heights[stack.pop()]
                if stack:
                    w=i-stack[-1]-1
                else:
                    w=i
                max_a=max(max_a,h*w)
            stack.append(i)
            
        return max_a


