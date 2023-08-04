"""
Table: Accounts
+-------------+------+
| Column Name | Type |
+-------------+------+
| account_id  | int  |
| income      | int  |
+-------------+------+

Calculate the number of bank accounts of each salary category. The salary categories are:

"Low Salary": All the salaries strictly less than $20000.
"Average Salary": All the salaries in the inclusive range [$20000, $50000].
"High Salary": All the salaries strictly greater than $50000.
The result table must contain all three categories. If there are no accounts in a category, return 0.

https://leetcode.com/problems/count-salary-categories/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
"""

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_count = len(accounts.loc[accounts['income'] < 20000])
    high_count = len(accounts.loc[accounts['income'] > 50000])
    avg_count = accounts.shape[0] - (high_count+low_count)

    df = pd.DataFrame()

    df['category'] = ['Low Salary', 'Average Salary', 'High Salary']
    df['accounts_count'] = [low_count, avg_count, high_count]

    return df
