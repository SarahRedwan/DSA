class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stacks=[]
        stackt=[]

        for i in s :
            if i=='#':
                if stacks:
                    stacks.pop()
            else:
                stacks.append(i)
        st="".join(stacks)
        for j in t:
            if j=='#':
                if stackt:
                    stackt.pop()
            else:
                stackt.append(j)
        tt="".join(stackt)

        return st==tt