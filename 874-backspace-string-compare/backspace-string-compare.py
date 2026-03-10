class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stacks=[]
        stackt=[]

        for i in s:
            if i=="#" :
                if stacks:
                    stacks.pop()
            else:
                stacks.append(i)
        ss="".join(stacks)
        for j in t:
            if  j=="#" :
                if stackt:
                    stackt.pop()
            else:
                stackt.append(j)
        st="".join(stackt)

        return ss==st