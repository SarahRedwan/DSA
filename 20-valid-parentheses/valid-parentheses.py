class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pair={')':'(','}':'{',']':'['}

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack or pair[ch]!=stack[-1]:
                    return False
                stack.pop()

        return len(stack)==0