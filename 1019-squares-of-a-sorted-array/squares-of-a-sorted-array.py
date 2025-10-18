class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)-1
        for i in range(len(nums)):
            nums[i]*=nums[i]
        nums.sort()
                


        return nums
