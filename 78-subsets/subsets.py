class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def breaktrack(i,path):
            if i==len(nums):
                res.append(path[:])
                return

            path.append(nums[i])
            breaktrack(i+1,path)
            path.pop()
            breaktrack(i+1,path)

        
        breaktrack(0,[])
        return res

