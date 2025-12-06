class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n=len(boxes)
        move=0
        ball=0
        ans=[0]*n
        for i in range(n):
            ans[i]+=move
            if boxes[i]=='1':
                ball+=1
            move+=ball
        move=0
        ball=0
        for i in range(n-1,-1,-1):
            ans[i]+=move
            if boxes[i]=='1':
                ball+=1
            move+=ball
        return ans
