class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq={}
        count=0
        left=0
        max_len=0

        for right in range(len(s)):
            if s[right] not in freq:
                freq[s[right]]=0
            if  freq[s[right]]==0:
                count+=1
            freq[s[right]]+=1

            while freq[s[right]]>1:
                freq[s[left]]-=1
                left+=1
            
            max_len=max(max_len,right-left+1)
        return max_len

