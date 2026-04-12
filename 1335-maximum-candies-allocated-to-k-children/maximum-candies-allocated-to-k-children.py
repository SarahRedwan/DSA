class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l=1
        r=max(candies)
        ans=0

        while l<=r:
            mid=(l+r)//2
            total=0
            for c in candies:
                total+=c//mid

            if total>=k:
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans
        


