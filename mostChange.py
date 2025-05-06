import sqlite3
from datetime import datetime

# Connect SQLite database
conn = sqlite3.connect("polygon_stock_data.db")
cursor = conn.cursor()


query = """
WITH sorted_prices AS (
    SELECT 
        date,
        strftime('%Y-%m', date) AS year_month,
        open,
        close,
        ROW_NUMBER() OVER (PARTITION BY strftime('%Y-%m', date) ORDER BY date ASC) AS rn_first,
        ROW_NUMBER() OVER (PARTITION BY strftime('%Y-%m', date) ORDER BY date DESC) AS rn_last
    FROM stock_prices
),
monthly_data AS (
    SELECT
        year_month,
        MAX(CASE WHEN rn_first = 1 THEN open END) AS open_first_day,
        MAX(CASE WHEN rn_last = 1 THEN close END) AS close_last_day
    FROM sorted_prices
    GROUP BY year_month
)
SELECT 
    year_month,
    open_first_day,
    close_last_day,
    ROUND(((close_last_day - open_first_day) / open_first_day) * 100, 2) AS percent_change
FROM monthly_data
ORDER BY percent_change DESC
LIMIT 5;
"""

cursor.execute(query)
results = cursor.fetchall()

if results:
    print(" Top 5 Months with Highest % Price Change:")
    for i, (month, open_price, close_price, percent_change) in enumerate(results, start=1):
        print(f"{i}. 📅 {month} | 🟢 Open: {open_price} | 🔴 Close: {close_price} | 🔺 Change: {percent_change}%")
else:
    print("No data found.")

conn.close()
