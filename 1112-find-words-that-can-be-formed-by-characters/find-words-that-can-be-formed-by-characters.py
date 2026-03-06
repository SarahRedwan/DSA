class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ch={}
        res=0

        for char in chars:
            ch[char]=ch.get(char,0)+1

        for word in words:
            copy=ch.copy()

            for c in word:
                if c in copy and copy[c]!=0:
                    copy[c]-=1
                else:
                    res-=len(word)
                    break
            res+=len(word)
        return res   