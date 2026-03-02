class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        

        left1 = 0
        count1 = 0
        dict1 = defaultdict(int)
        
        left2 = 0
        count2 = 0
        dict2 = defaultdict(int)

        for right in range(len(nums)):

            dict1[nums[right]] += 1
            dict2[nums[right]] += 1

            while len(dict1) > k:
                dict1[nums[left1]] -= 1
                if dict1[nums[left1]] == 0:
                    del dict1[nums[left1]]
                left1 += 1


            while len(dict2) > k - 1:
                dict2[nums[left2]] -= 1
                if dict2[nums[left2]] == 0:
                    del dict2[nums[left2]]
                left2 += 1

            count1 += right - left1 + 1
            count2 += right - left2 + 1

        return count1 - count2