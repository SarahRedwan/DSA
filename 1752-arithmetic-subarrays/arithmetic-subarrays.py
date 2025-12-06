class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans=[]

        for i in range(len(l)):
            sub=nums[l[i]:r[i]+1]
            sub.sort()
            diff=sub[1]-sub[0]

            ok=True

            for j in range(2,len(sub)):
                if sub[j]-sub[j-1]!=diff:
                    ok=False
                    break

            ans.append(ok)
        return ans



            
