from collections import Counter
class Solution(object):
    def findValidPair(self, s):
        s_count = Counter(s)

        left = 0
        right = 1
      
        while right < len(s):
            if s[left] != s[right] and s_count[s[left]] == int(s[left]) and s_count[s[right]] == int(s[right]):
                return s[left] + s[right]
            else:
                left += 1
                right += 1
        else:
            return ""