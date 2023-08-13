"""
Table: Courses
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student     | varchar |
| class       | varchar |
+-------------+---------+

Write a solution to find all the classes that have at least five students.
Return the result table in any order.
"""

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby('class').count().reset_index()
    return df[df['student'] >= 5][['class']]
