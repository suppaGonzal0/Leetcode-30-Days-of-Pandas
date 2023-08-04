"""
Table: Store
+-------------+------+
| Column Name | Type |
+-------------+------+
| bill_id     | int  |
| customer_id | int  |
| amount      | int  |
+-------------+------+
 
Report the number of customers who had at least one bill with an amount strictly greater than 500.

https://leetcode.com/problems/the-number-of-rich-customers/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
"""

import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(data=[store[store['amount'] > 500]['customer_id'].unique().shape[0]], columns=['rich_count'])
