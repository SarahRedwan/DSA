class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        
        def backtrack(start, path):
            if len(path) >= 2:
                res.add(tuple(path))
            for i in range(start, len(nums)):
                if not path or nums[i] >= path[-1]:
                    backtrack(i+1, path+[nums[i]])
        
        backtrack(0, [])
        return [list(x) for x in res]
