class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        used=[0]*len(nums)

        def backtrack(path):
            if len(path)==len(nums):
                res.append(path[:])
                return 
            for i in range(len(nums)):
                if not used[i]:
                    used[i]=1
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
                    used[i]=0
        backtrack([])

        return res
                
