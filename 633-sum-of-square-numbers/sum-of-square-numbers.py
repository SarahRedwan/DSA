class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        right=int(c**0.5)
        left=0
        while left<=right:
            if right*right+left*left==c:
                return True
            elif right*right+left*left<c:
                left+=1
            elif right*right+left*left>c :
                right-=1

        return False

        