class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3!=0:
            return []
        first=num//3 -1
        return [first,first+1,first+2]


        
        