"""
Table: Activity

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+

Write a solution to find the first login date for each player.
Return the result table in any order.
"""

import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return activity.groupby(
        'player_id'
    ).agg(
        first_login=('event_date', 'min')
    ).reset_index()
