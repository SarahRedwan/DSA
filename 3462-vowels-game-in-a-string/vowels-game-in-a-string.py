class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for _ in s:
            if _ in "aeiou":
                return True 
        return False