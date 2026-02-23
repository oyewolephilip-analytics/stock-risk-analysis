#!/usr/bin/env python
# coding: utf-8

# # Historical Value at Risk (VaR) Analysis of JPMORGAN and NVIDIA

# This notebook analyzes the daily risk of JPMorgan Chase (JPM) and NVIDIA(NVDA) stocks using historical simulation and Value at Risk (VaR)

# ## 1. Import Libaries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.savefig('chart.png')


# ## 2. Load and Prepare Data

# The dataset contains one year of daily closing prices for JPMorgan and NVIDIA.The Date column is converted to a datetime index for time-series analysis.

# In[2]:


JPMORGAN = pd.read_csv(r"C:\Users\dell\Documents\Project files\JPMorgan.csv")
print(JPMORGAN.head())


# In[3]:


nvidia = pd.read_csv(r"C:\Users\dell\Documents\Project files\nvidia.csv")
print(nvidia.head())


# In[4]:


JPMORGAN['Date'] = pd.to_datetime(JPMORGAN['Date'])
nvidia['Date'] = pd.to_datetime(nvidia['Date'])

JPMORGAN.set_index('Date', inplace=True)
nvidia.set_index('Date', inplace=True)


# In[5]:


JPMORGAN = JPMORGAN[['Close']].rename(columns={'Close': 'JPMORGAN'})
nvidia = nvidia[['Close']].rename(columns={'Close': 'nvidia'})


# In[6]:


prices = pd.merge(JPMORGAN, nvidia, left_index=True, right_index=True, how='inner')
print(prices.head())


# ## 3. Daily Percentage Returns 

# Daily returns show how much the stock price changes from one trading day to the next.

# In[7]:


returns = prices.pct_change().dropna()
print(returns.head())


# In[8]:


print(prices.head())
print(prices.columns)


# ## 4. Historical Simulation and Value at Risk (VaR)

# Historical simulation ranks past returns from worst to best to estimate potential losses.

# In[9]:


JPMORGAN_returns = returns['JPMORGAN']
nvidia_returns = returns['nvidia']

JPMORGAN_sorted = JPMORGAN_returns.sort_values()
nvidia_sorted = nvidia_returns.sort_values()


# In[10]:


import numpy as np

JPMORGAN_var_5 = np.percentile(JPMORGAN_returns, 5)
nvidia_var_5 = np.percentile(nvidia_returns, 5)

print("JPMORGAN 5% VaR:", JPMORGAN_var_5)
print("nvidia 5% VaR:", nvidia_var_5)


# In[11]:


import matplotlib.pyplot as plt

plt.figure()
plt.hist(JPMORGAN_returns, bins=50)
plt.axvline(JPMORGAN_var_5)
plt.title("JPMORGAN Daily Returns Distribution")
plt.xlabel("Daily Return")
plt.ylabel("Frquency")
plt.savefig('risk_chart.png')


# In[12]:


plt.figure()
plt.hist(nvidia_returns, bins=50)
plt.axvline(nvidia_var_5)
plt.title("Nvidia Daily Returns Distribution")
plt.xlabel("Daily Return")
plt.ylabel("Frequency")
plt.savefig('risk_chart.png')


# ## 5. Portfolio Value at Risk

# ### Diversification Effect
# 
# Although NVIDIA exhibits higher volatility and downside risk compared to JPMorgan,combining both stocks into a 50/50 portfolio reduces overall portfolio risk.
# 
# This occurs because the two stocks do not move exactly the same way every day.Losses in one stock are sometimes offset by gains or smaller losses in the other,leading to a smoother return distribution and lower Value at Risk (VaR).

# In[13]:


weights = np.array([0.5, 0.5])


# In[14]:


portfolio_returns = returns.dot(weights)
print(portfolio_returns.head())


# In[15]:


portfolio_sorted = portfolio_returns.sort_values()


# In[16]:


portfolio_var_5 = np.percentile(portfolio_returns, 5)
print("Portfolio 5% VaR:", portfolio_var_5)


# In[17]:


plt.figure()
plt.hist(portfolio_returns, bins=50)
plt.axvline(portfolio_var_5)
plt.title("Portfolio Daily Returns Distribution")
plt.xlabel("Daily Return")
plt.ylabel("Frquency")
plt.savefig('risk_chart.png')


# In[18]:


print("JPMORGAN VaR:", JPMORGAN_var_5)
print("nvidia VaR:", nvidia_var_5)
print("portfolio VaR:", portfolio_var_5)


# ## 6. Conclusion

# ## Conclusion
# 
# This analysis applied historical simulation and Value at Risk (VaR) to evaluate the downside risk of JPMorgan and NVIDIA stocks using one year of historical data.
# 
# The results show that NVIDIA has higher volatility and greater downside risk,while JPMorgan is relatively more stable. When combined into a portfolio,
# overall risk is reduced due to diversification effects.
# 
# This project demonstrates how Python can be used to analyze financial risk,evaluate portfolio performance, and support data-driven investment decisions.
