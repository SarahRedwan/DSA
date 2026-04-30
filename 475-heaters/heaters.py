from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        def nearest_heater(house: int) -> int:
            l, r = 0, len(heaters) - 1
            while l <= r:
                mid = (l + r) // 2
                if heaters[mid] == house:
                    return 0
                elif heaters[mid] < house:
                    l = mid + 1
                else:
                    r = mid - 1
            
            
            if r < 0:
                left_dist = float('inf')
            else:
                left_dist = house - heaters[r]
            
            if l >= len(heaters):
                right_dist = float('inf')
            else:
                right_dist = heaters[l] - house
            
            return min(left_dist, right_dist)
        
        radius = 0
        for house in houses:
            radius = max(radius, nearest_heater(house))
        
        return radius
