class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new=sorted(heights)
        count=0
        for i in range(len(heights)):
            if new[i]!=heights[i]:
                count+=1
        return count