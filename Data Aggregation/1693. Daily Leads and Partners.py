"""
Table: DailySales
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| date_id     | date    |
| make_name   | varchar |
| lead_id     | int     |
| partner_id  | int     |
+-------------+---------+
 
For each date_id and make_name, find the number of distinct lead_id's and distinct partner_id's.

https://leetcode.com/problems/daily-leads-and-partners/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
"""

import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    return daily_sales.groupby(
        ['date_id', 'make_name']
    ).nunique().reset_index().rename(columns={
        'lead_id': 'unique_leads',
        'partner_id': 'unique_partners',
    })
