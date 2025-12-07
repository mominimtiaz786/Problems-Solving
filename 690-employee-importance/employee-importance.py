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

        hashmap = {emp.id:emp for emp in employees}
        req_employee = hashmap[id]
        
        assert req_employee

        q = [id]
        total_importance = 0
        while q:
            emp = hashmap[q.pop(0)]
            total_importance+=emp.importance

            q+=emp.subordinates
        return total_importance

        