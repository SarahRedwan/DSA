class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        unique_chars = set(s)
        
        for i in unique_chars:
            if s.count(i) != t.count(i):
                return False
                
        return True