class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack=[]
        for i in range(len(prices)):
            discount=0
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    discount+=prices[j]
                    break
            stack.append(prices[i]-discount)
        return stack
