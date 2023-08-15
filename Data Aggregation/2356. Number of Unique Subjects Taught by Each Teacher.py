"""
Table: Teacher
+-------------+------+
| Column Name | Type |
+-------------+------+
| teacher_id  | int  |
| subject_id  | int  |
| dept_id     | int  |
+-------------+------+

Write a solution to calculate the number of unique subjects each teacher teaches in the university.
"""

import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return teacher.groupby(
        'teacher_id'
    )['subject_id'].nunique().reset_index().rename(
        columns={'subject_id': 'cnt'}
    )[['teacher_id', 'cnt']]
