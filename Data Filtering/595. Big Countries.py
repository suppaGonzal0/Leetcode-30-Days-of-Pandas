"""
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |
+-------------+---------+

Write a solution to find the ids of products that are both low fat and recyclable.
Return the result table in any order.
The result format is in the following example.
"""

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world[['name', 'population', 'area']]
    return df[(df['area'] >= 3000000) | ( df['population'] >= 25000000)]
