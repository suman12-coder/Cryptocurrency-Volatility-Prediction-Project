#  Exploratory Data Analysis (EDA) – Cryptocurrency Volatility Prediction

##  Objective
The goal of this analysis is to understand the structure, distribution, and relationships within the cryptocurrency dataset and identify key patterns that influence price volatility.

---

##  Dataset Overview

**Columns:**
- `open` – Opening price of the cryptocurrency on that date  
- `high` – Highest price reached during the day  
- `low` – Lowest price reached during the day  
- `close` – Closing price of the cryptocurrency  
- `volume` – Total trading volume during the day  
- `marketCap` – Total market capitalization of the cryptocurrency  
- `timestamp` – Unix timestamp of the record  
- `crypto_name` – Name of the cryptocurrency  
- `date` – Date of the record  

**Shape:**  
→ Rows: varies (~70,000)  
→ Columns: 9 (plus derived features later)

---

## Missing Values and Data Cleaning
- Checked for missing values using `df.isnull().sum()`  
- Found and handled nulls in columns like `marketCap` and `volume`
- Remove Unnecessary column like `Unnamed: 0` 
- Filled or dropped rows where missing values exceeded acceptable limits  
- Removed duplicates based on `date` and `crypto_name`  


---

## Data Distribution
- Most cryptocurrencies showed right-skewed distributions in `volume` and `marketCap`  
- Price features (`open`, `close`) displayed high variance  
- Normalized data later using `MinMaxScaler`
- Distribution of closing prices data is highly right-skewed, meaning most closing prices are concentrated on the lower end of the scale.

# Countplot for crypto_name
- Bitcoin has the highest count, indicating it's the most frequently mentioned or traded cryptocurrency in this dataset.
- After Bitcoin, the next most frequent names are Litecoin, Ethereum, Dogecoin, and Stellar.
- Cryptos like Ripple, Monero, and Dash show moderate frequency, suggesting niche popularity or specialized use cases (e.g., privacy, speed).
- Coins like Apollo, Civic, Golem, and Qtum have very low counts. These may be newer, less adopted, or inactive projects.

# Volume vs Closing price scatter plot
- Dense Cluster at Low Volume: Most data points are concentrated at low trading volumes, with a wide spread of closing prices (mostly below 10,000).

- Sparse High-Volume Region: As trading volume increases, the number of data points drops sharply. This indicates that high-volume trades are rare.
- Outliers: A few points show extremely high trading volumes and closing prices.
-  Correlation Insight: There's no clear linear trend between volume and closing price.

  ### Opening vs Closing Price scatter plot

- Core Observations: Strong Positive Correlation between open and close prices columns.The data points form a tight diagonal band from bottom-left to top-right, indicating that opening and closing prices are closely aligned. This suggests that for most entries, the price didn’t fluctuate drastically during the trading period.

  
---

##  Correlation Analysis
- Strong positive correlation between `open`, `close`, `high`, and `low`
-  Market capitalization shows a moderate-to-strong correlation (0.67) with all price metrics.
-  Volume has a moderate correlation (0.46) with market cap, suggesting that larger-cap assets may attract more trading activity

- Weak or moderate correlation between `volume` and price-related features
- Generated heatmap using:
  ```python
  sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
