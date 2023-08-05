"""
Table: Employee
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+

Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

https://leetcode.com/problems/nth-highest-salary/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
"""

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salary = employee.sort_values('salary', ascending=False)['salary'].drop_duplicates().reset_index(drop=True)
    print(salary)
    if N > len(salary):
        return pd.DataFrame(data=[None], columns=[f'getNthHighestSalary({N})'])

    return pd.DataFrame(data=[salary[N-1]], columns=[f'getNthHighestSalary({N})'])
