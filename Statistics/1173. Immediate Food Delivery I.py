"""
Table: Delivery

+-----------------------------+---------+
| Column Name                 | Type    |
+-----------------------------+---------+
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |
+-----------------------------+---------+

If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.

Find the percentage of immediate orders in the table, rounded to 2 decimal places.

https://leetcode.com/problems/immediate-food-delivery-i/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
"""

import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    df = delivery[delivery['order_date'] == delivery['customer_pref_delivery_date']]
    percentage = round(df.shape[0]*100/delivery.shape[0],2)
    return pd.DataFrame({'immediate_percentage':[percentage]})
