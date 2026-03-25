class Solution:
    def lastRemaining(self, n: int) -> int:
        nums=n
        start=1
        step=1

        left_to_right=True
        while nums>1:
            if left_to_right or nums%2==1:
                start+=step
            
            step*=2
            nums//=2
            left_to_right=not left_to_right
        return start

        