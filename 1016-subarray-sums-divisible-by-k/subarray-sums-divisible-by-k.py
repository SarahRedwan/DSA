class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        curr=0
        count=0
        freq={0:1}

        for num in nums:
            curr+=num
            rem=curr%k
            if rem in freq:
                count+=freq[rem]
            
            freq[rem]=freq.get(rem,0)+1
        return count