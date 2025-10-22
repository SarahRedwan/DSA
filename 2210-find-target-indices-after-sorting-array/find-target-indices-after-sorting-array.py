class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        result=[]
        i=0
        while i<len(nums)-1:
            if nums[i]>nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]
                i=0
            else:
                i+=1
            
        for num in range(len(nums)):
            if nums[num]==target:
                result.append(num)

        return result