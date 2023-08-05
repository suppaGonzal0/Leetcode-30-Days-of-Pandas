"""
Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+

Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

https://leetcode.com/problems/second-highest-salary/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
"""

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salary = employee.sort_values('salary', ascending=False)['salary'].drop_duplicates().reset_index(drop=True)
    print(salary)
    if 2 > len(salary):
        return pd.DataFrame(data=[None], columns=['SecondHighestSalary'])

    return pd.DataFrame(data=[salary[1]], columns=['SecondHighestSalary'])
