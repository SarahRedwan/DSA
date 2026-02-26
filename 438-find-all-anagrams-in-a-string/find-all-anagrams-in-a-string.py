from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):   # guard clause
            return []

        p_counter = Counter(p)
        window_counter = Counter()
        result = []
        k = len(p)

        # Step 1: initialize the first window
        for i in range(k):
            window_counter[s[i]] += 1
        if window_counter == p_counter:
            result.append(0)

        left = 0
        # Step 2: slide the window
        for right in range(k, len(s)):
            window_counter[s[right]] += 1
            window_counter[s[left]] -= 1
            if window_counter[s[left]] == 0:
                del window_counter[s[left]]
            left += 1

            if window_counter == p_counter:
                result.append(left)

        return result
