"""
Table: Employees
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
| salary      | int     |
+-------------+---------+

Write a solution to calculate the bonus of each employee. 
The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee's name does not start with the character 'M'.
The bonus of an employee is 0 otherwise.
Return the result table ordered by employee_id.

https://leetcode.com/problems/calculate-special-bonus/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
"""

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(
        lambda row: 
            row['salary'] if row['employee_id'] % 2 == 1 and row['name'][0] != 'M' 
            else 0, 
        axis=1
    )
    return  employees[['employee_id', 'bonus']].sort_values(by='employee_id')
    
