class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack=[]
        ans=[]

        for i in range(len(nums)):
            while stack and stack[0][1]<=i-k:
                stack.pop(0)
            while stack and nums[i]>stack[-1][0]:
                stack.pop()
            stack.append([nums[i],i])

            if i>=k-1:
                ans.append(stack[0][0])

        return ans



        