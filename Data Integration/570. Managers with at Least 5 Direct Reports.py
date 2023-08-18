"""
Table: Employee
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
 
Write a solution to find managers with at least five direct reports.
"""

import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    managers = employee.groupby(
        'managerId', as_index=False
    ).agg(
        reporting=('id', 'count'),
    ).query(
        '5 <= reporting'
    )['managerId']

    return employee[
        employee['id'].isin(managers)
    ][['name']]
