class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def daynums(capacity):
            c=0
            d=0
            for i in weights:
                c+=i
                if c>capacity:
                    d+=1
                    c=i
            
            return d+1<=days

        low=max(weights)-1
        high=sum(weights)

        d=0
        while low+1<high:
            mid=(low+high)//2
            # print(mid, daynums(mid))

            if not daynums(mid):
                low=mid
            else:
                high=mid
            
        return high