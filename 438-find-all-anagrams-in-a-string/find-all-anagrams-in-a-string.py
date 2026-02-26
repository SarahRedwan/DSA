from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        p_counter = Counter(p)
        window_counter = Counter()
        result = []
        k = len(p)

        
        for i in range(k):
            window_counter[s[i]] += 1
        if window_counter == p_counter:
            result.append(0)

        left = 0
        for right in range(k, len(s)):
            window_counter[s[right]] += 1
            window_counter[s[left]] -= 1
            if window_counter[s[left]] == 0: 
                del window_counter[s[left]]
            left += 1

            if window_counter == p_counter:
                result.append(left)

        return result
