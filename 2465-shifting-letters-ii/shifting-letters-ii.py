class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n=len(s)
        diff=[0]*(n+1)

        for start,end,direction in shifts:
            if direction==1:
                diff[start]+=1
                diff[end+1]-=1
            else:
                diff[start]-=1
                diff[end+1]+=1
        for i in range(1,n):
            diff[i]+=diff[i-1]
        res=[]
        for i in range(n):
            shift=diff[i]%26
            new_char=chr((ord(s[i])-ord('a')+shift)%26 +ord('a'))
            res.append(new_char)
        
        return "".join(res)

