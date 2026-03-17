class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n==1:
            return x
        if n==0:
            return 1
        
        if n<0:
            return 1/(x* self.myPow(x,(-n)-1))

        if n%2==0:
            res=self.myPow(x,n//2)
            return res*res
        else:
            res=self.myPow(x,(n-1)//2)
            return x*res*res

    