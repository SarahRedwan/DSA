class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res=0
        rabbits={}
        for i in answers:
            if i not in rabbits or rabbits[i]==0:
                rabbits[i]=i
                res+=i+1
            else:
                rabbits[i]-=1

        return res
