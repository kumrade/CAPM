Capital Asset Pricing Model

data.py downloads historical stock data for Infosys (INFY.NS) and TCS (TCS.NS) using Yahoo Finance. It converts the specified date range (December 1-31, 2023) into Unix timestamps, fetches the data via API, and saves the results as CSV files in the current directory.

main.py retrieves data for Infosys, TCS, and the NIFTY 50 index (^NSEI) for the same period. It visualizes the closing prices and cumulative returns, calculates daily returns, and performs linear regression to compute beta and alpha values for Infosys and TCS relative to the NIFTY 50 index. This helps assess the stocks' sensitivity and performance compared to the market.
