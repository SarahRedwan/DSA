class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res=set()

        l=0
        r=0

        for c in s:
            if c=="(":
                l+=1
            elif c==")":
                if l>0:
                    l-=1
                else:
                    r+=1

        def dfs(i,path,open_count,l,r):
            
            if i==len(s):
                if l==0 and r==0 and open_count==0:
                    res.add(path)
                return
            c=s[i]

            if c=="(":
                if l>0:
                    dfs(i+1,path,open_count,l-1,r)
                dfs(i+1,path+c,open_count+1,l,r)
            elif c==")":
                if r>0:
                    dfs(i+1,path,open_count,l,r-1)
                if open_count>0:
                    dfs(i+1,path+c,open_count-1,l,r)
            else:
                dfs(i+1,path+c,open_count,l,r)

        dfs(0,"",0,l,r)
        return list(res)
