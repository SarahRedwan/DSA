class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h=0
        a=citations.sort(reverse=True)

        for i in range(len(citations)):
            if citations[i]>=i+1:
                h=i+1
            else:
                break
        return h