import requests
import time

# Set date range for December 2023
stat_time = "2023-12-01"
ending_time = "2023-12-31"

# Convert the dates into Unix timestamps
start_array = time.strptime(stat_time, "%Y-%m-%d")
ending_array = time.strptime(ending_time, "%Y-%m-%d")
start_stamp = int(time.mktime(start_array))
ending_stamp = int(time.mktime(ending_array))

# NIFTY stock codes (example: INFY = Infosys, TCS = Tata Consultancy Services)
stock_codes = ["INFY.NS", "TCS.NS"]

# Set period1 and period2 for timestamps
period1 = start_stamp
period2 = ending_stamp

# Loop through the stock codes and download data for each
for stock_code in stock_codes:
    url = """https://query1.finance.yahoo.com/v7/finance/download/{}?period1={}&period2={}&interval=1d&events=history&includeAdjustedClose=true""".format(
        stock_code, period1, period2)
    
    # Send request to Yahoo Finance
    response = requests.get(url=url)
    
    # Define filename and save the CSV
    filename = stock_code + ".csv"
    print(filename + " downloading")
    
    with open(filename, "wb") as f:
        f.write(response.content)

    print(f"Downloaded data for {stock_code}")
