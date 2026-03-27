class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def breaktrack(i,path):
            if i==len(nums):
                res.append(path[:])
                return 
            path.append(nums[i])
            breaktrack(i+1,path)
            path.pop()

            
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
                
            breaktrack(i+1,path)
        
        breaktrack(0,[])
        return res
