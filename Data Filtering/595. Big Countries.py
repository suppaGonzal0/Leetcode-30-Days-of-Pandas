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
name is the primary key (column with unique values) for this table.
Each row of this table gives information about the name of a country, the continent to which it belongs, its area, the population, and its GDP value.  
"""

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    big_countries = world[['name', 'population', 'area']]
    return big_countries[(big_countries['area'] >= 3000000) | ( big_countries['population'] >= 25000000)]
