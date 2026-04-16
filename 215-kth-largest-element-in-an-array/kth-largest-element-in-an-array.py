class Solution:
    def findKthLargest(self, nums, k):
        
        def quickselect(nums, k):
            pivot = nums[0]
            left, mid, right = [], [], []

            for x in nums:
                if x > pivot:
                    left.append(x)
                elif x < pivot:
                    right.append(x)
                else:
                    mid.append(x)

            if k <= len(left):
                return quickselect(left, k)
            elif k <= len(left) + len(mid):
                return pivot
            else:
                return quickselect(right, k - len(left) - len(mid))

        return quickselect(nums, k)