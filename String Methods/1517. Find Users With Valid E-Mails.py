"""
Table: Users
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
| mail          | varchar |
+---------------+---------+

Find the users who have valid emails.

A valid e-mail has a prefix name and a domain where:
  1. The prefix name is a string that may contain letters (upper or lower case), digits, underscore '_', period '.', and/or dash '-'. The prefix name must start with a letter.
  2. The domain is '@leetcode.com'.
  3. Return the result table in any order.

https://leetcode.com/problems/find-users-with-valid-e-mails/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
"""

import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users.loc[users['mail'].str.contains('^[A-Za-z]+[A-Za-z\d\_\.\-]*@leetcode\.com$', regex=True)]
