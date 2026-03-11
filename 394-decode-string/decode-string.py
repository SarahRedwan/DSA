class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i]!="]":
                stack.append(s[i])
            else:
                word=""
                while stack and stack[-1]!="[":
                    word=stack.pop()+word
                stack.pop()
                num=[]
                while stack and stack[-1].isdigit():
                    num+=stack.pop()
                    num.reverse()
                stack.append(int("".join(num))*word)
                        
        return "".join(stack)