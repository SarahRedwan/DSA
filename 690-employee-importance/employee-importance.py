"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_map = {emp.id: emp for emp in employees}
        
        def dfs(id):
            imp = emp_map[id].importance
            for j in emp_map[id].subordinates:
                imp += dfs(j)
                
            return imp
        
        return dfs(id)