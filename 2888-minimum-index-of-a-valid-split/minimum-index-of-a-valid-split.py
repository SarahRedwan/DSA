from collections import Counter

class Solution:
    def minimumIndex(self, nums):
        n = len(nums)
        cnt = Counter(nums)
        dom = max(cnt, key=cnt.get)
        total = cnt[dom]

        left_count = 0

        for i in range(n - 1):
            if nums[i] == dom:
                left_count += 1

            right_count = total - left_count

            if left_count * 2 > (i + 1) and right_count * 2 > (n - i - 1):
                return i

        return -1