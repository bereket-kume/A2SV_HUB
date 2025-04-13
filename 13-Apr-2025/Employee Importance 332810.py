# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

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
        em = defaultdict(int)

        for emp in employees:
            em[emp.id] = emp
        print(em)

        def dfs(emp_id):
            emp = em[emp_id]
            ans = emp.importance

            for i in emp.subordinates:
                ans += dfs(i)
            return ans
        return dfs(id)