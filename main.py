from scipy import stats
import pandas_datareader as web
import datetime
import matplotlib.pyplot as plt

# Set date range (December 2023)
start = datetime.datetime(2023, 12, 1)
end = datetime.datetime(2023, 12, 31)

# Retrieve data for NIFTY 50 index (^NSEI), Infosys (INFY.NS), and TCS (TCS.NS)
df_nifty = web.DataReader('^NSEI', 'yahoo', start, end)
df_infy = web.DataReader('INFY.NS', 'yahoo', start, end)
df_tcs = web.DataReader('TCS.NS', 'yahoo', start, end)

# Display the first few rows of data
print(df_nifty.head())
print(df_infy.head())
print(df_tcs.head())

# Plot the 'Close' prices for both stocks
df_infy['Close'].plot(label='Infosys', figsize=(10, 8))
df_tcs['Close'].plot(label='TCS')
plt.legend()
plt.title('Closing Prices of Infosys and TCS in December 2023')
plt.show()

# Calculate cumulative returns
df_infy['Cumu'] = df_infy['Close'] / df_infy['Close'].iloc[0]
df_tcs['Cumu'] = df_tcs['Close'] / df_tcs['Close'].iloc[0]
df_nifty['Cumu'] = df_nifty['Close'] / df_nifty['Close'].iloc[0]

# Plot cumulative returns
df_infy['Cumu'].plot(label='Infosys', figsize=(10, 8))
df_tcs['Cumu'].plot(label='TCS')
df_nifty['Cumu'].plot(label='NIFTY 50')
plt.legend()
plt.title('Cumulative Returns of Infosys, TCS, and NIFTY 50 in December 2023')
plt.show()

# Calculate daily returns for Infosys, TCS, and NIFTY 50
df_infy['daily_ret'] = df_infy['Close'].pct_change(1)
df_tcs['daily_ret'] = df_tcs['Close'].pct_change(1)
df_nifty['daily_ret'] = df_nifty['Close'].pct_change(1)

# Scatter plot of daily returns for Infosys vs NIFTY 50
plt.scatter(df_infy['daily_ret'], df_nifty['daily_ret'])
plt.title('Daily Returns: Infosys vs NIFTY 50')
plt.xlabel('Infosys Daily Return')
plt.ylabel('NIFTY 50 Daily Return')
plt.show()

# Scatter plot of daily returns for TCS vs NIFTY 50
plt.scatter(df_tcs['daily_ret'], df_nifty['daily_ret'])
plt.title('Daily Returns: TCS vs NIFTY 50')
plt.xlabel('TCS Daily Return')
plt.ylabel('NIFTY 50 Daily Return')
plt.show()

# Perform linear regression to calculate beta and alpha for Infosys
LR_infy = stats.linregress(df_infy['daily_ret'].iloc[1:], df_nifty['daily_ret'].iloc[1:])
beta_infy, alpha_infy, r_val_infy, p_val_infy, std_err_infy = LR_infy

# Perform linear regression to calculate beta and alpha for TCS
LR_tcs = stats.linregress(df_tcs['daily_ret'].iloc[1:], df_nifty['daily_ret'].iloc[1:])
beta_tcs, alpha_tcs, r_val_tcs, p_val_tcs, std_err_tcs = LR_tcs

# Output beta and alpha for Infosys
print("Infosys Beta:", beta_infy)
print("Infosys Alpha:", alpha_infy)

# Output beta and alpha for TCS
print("TCS Beta:", beta_tcs)
print("TCS Alpha:", alpha_tcs)
