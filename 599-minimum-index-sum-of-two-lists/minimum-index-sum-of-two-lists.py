class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        min_index= float(inf)
        for i in range(len(list1)):
            if list1[i] in list2:
                j = list2.index(list1[i]) 
                if i + j < min_index:
                    min_index = i + j
                    ans = [list1[i]]
                elif i+j==min_index:
                    ans.append(list1[i])
        return ans