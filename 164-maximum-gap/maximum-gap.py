from typing import List
import math

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        n = len(nums)
        mn, mx = min(nums), max(nums)
        range1=mx-mn
        
        if mn == mx:
            return 0
        
        buckets = [[] for _ in range(n+1)]
        
        for num in nums:
            idx = (int(n*(num - mn) )// range1)
            buckets[idx].append(num)
        
        prev_max = None
        max_gap = 0
        
        for bucket in buckets:
            if not bucket:
                continue
            
            current_min = min(bucket)
            current_max = max(bucket)
            
            if prev_max is not None:
                max_gap = max(max_gap, current_min - prev_max)
            
            prev_max = current_max
        
        return max_gap