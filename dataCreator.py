import requests
import sqlite3
import time

# please install requests
# you can widen the range of data here but im not sure is it gonna work due to polygon.io api request limit
API_KEY = "THMYthIWdAAfEttxcY9cPHRAgkiOFFrS"
symbol = "AAPL"
start_date = "2020-01-01"
end_date = "2024-01-01"

# Create SQLite DB
conn = sqlite3.connect("polygon_stock_data.db")
cursor = conn.cursor()
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS stock_prices (
    date TEXT PRIMARY KEY,
    open REAL,
    close REAL
)
"""
)


# fetch
def fetch_data(url, params):
    data = []
    while True:
        response = requests.get(url, params=params)
        json_data = response.json()
        if "results" in json_data:
            data.extend(json_data["results"])
            if "next" in json_data:
                params["page"] = json_data["next"]
            else:
                break
        else:
            print("❌ Error or no results:", json_data)
            break
    return data


# Pull data from Polygon.io
url = f"https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/day/{start_date}/{end_date}"
params = {
    "adjusted": "true",
    "sort": "asc",
    "limit": 50000,
    "apiKey": API_KEY,
    "page": 1,
}

data = fetch_data(url, params)

# Insert data into SQLite
if data:
    for day in data:
        date = time.strftime("%Y-%m-%d", time.gmtime(day["t"] / 1000))
        open_price = day["o"]
        close_price = day["c"]
        cursor.execute(
            "INSERT OR IGNORE INTO stock_prices (date, open, close) VALUES (?, ?, ?)",
            (date, open_price, close_price),
        )
    conn.commit()
    print("✅ Data inserted into SQLite.")
else:
    print("❌ No data found or error from Polygon API.")

conn.close()
