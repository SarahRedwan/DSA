class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last={c:i for i,c in enumerate(s)}
        start=0
        end=0
        result=[]

        for i,c in enumerate(s):
            end=max(end,last[c])
            if i==end:
                result.append(end-start+1)
                start=i+1
        return result

