from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        orginal=[]
        changed.sort()
        count=Counter(changed)

        if len(changed)%2!=0:
            return []
        
        for i in changed:
            if count[i]==0:
                continue
            if count[2*i]==0:
                return []

            orginal.append(i)
            count[i]-=1
            count[2*i]-=1
        return orginal
