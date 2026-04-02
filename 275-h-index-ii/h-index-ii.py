class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left=0
        right=len(citations)-1
        n=len(citations)
        while left<=right:
            mid=(left+right)//2

            if citations[mid]>=n-mid:
                right=mid-1
            else:
                left=mid+1
        return n-left