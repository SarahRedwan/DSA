class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        seen=set()
        duplicated=0
        
        for num in nums:
            if num in seen:
                duplicated=num
            else:
                seen.add(num)
        for i in range(1,n+1):
            if i not in seen:
                missed=i
                break
        
        return [duplicated,missed]



