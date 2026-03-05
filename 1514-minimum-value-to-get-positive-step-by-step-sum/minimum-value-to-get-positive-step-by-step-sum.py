class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        curr=0
        min_val=0

        for num in nums:
            curr+=num
            min_val=min(min_val,curr)
        
        return (1 - min_val)