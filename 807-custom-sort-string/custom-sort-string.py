class Solution:
    def customSortString(self, order: str, s: str) -> str:
        from collections import Counter
        freq=Counter(s)
        res=[]
        for c in order:
            if c in freq:
                res.append(c* freq[c])
                del freq[c]
        for c in freq:
            res.append(c* freq[c])
        return "".join(res)
