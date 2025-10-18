class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=0
        result=[]
        for i in nums:
            for j in nums:
                if j<i:
                    count+=1
            result.append(count)
            count=0

        return result

        