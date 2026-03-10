class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        nge = {}
        ans=[]
        for num in nums2:
            while stack and num>stack[-1]:
                nge[stack.pop()]=num
            stack.append(num)
        while stack:
            nge[stack.pop()]=-1
        for x in nums1:
            ans.append(nge[x])
        
        return ans
        
        
        