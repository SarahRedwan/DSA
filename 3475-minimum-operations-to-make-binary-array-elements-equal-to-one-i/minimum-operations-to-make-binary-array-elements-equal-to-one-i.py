class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res=0
        def flip(nums,i):
            nums[i]=0 if nums[i] else 1
       

        for i in range(len(nums)-2):
            if nums[i]==0:
                flip(nums,i)
                flip(nums,i+1)
                flip(nums,i+2)

                res+=1
        if not nums[-1] or not nums[-2]:
            return -1
        return res

            