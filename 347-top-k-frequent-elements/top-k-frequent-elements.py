class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        res=[]

        for _ in range(k):
            max_num = max(freq, key=freq.get)  
            res.append(max_num)
            del freq[max_num]  #
        return res