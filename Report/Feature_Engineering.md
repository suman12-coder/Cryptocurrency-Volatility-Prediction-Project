# Rolling Volatility:
   - Computes standard deviation of returns over 7-day and 30-day windows.
  - Measures short-term and long-term volatility.
   - min_periods=1 allows calculation even if fewer than 7 days exist at the start.
``` python
df['vol_7'] = df.groupby('crypto_name')['returns'].rolling(window=7, min_periods=1).std().reset_index(0, drop=True)
df['vol_30'] = df.groupby('crypto_name')['returns'].rolling(window=30, min_periods=1).std().reset_index(0, drop=True)
```

# Moving Avg:
  - Calculates average closing prices over 7 and 30 days.
  - Smooths short-term fluctuations → reveals trend direction.
  ``` python
df['ma_7'] = df.groupby('crypto_name')['close'].rolling(window=7, min_periods=1).mean().reset_index(0, drop=True)
df['ma_30'] = df.groupby('crypto_name')['close'].rolling(window=30, min_periods=1).mean().reset_index(0, drop=True)
```

# Price Range Features:
  - daily_range: difference between daily high and low → how much the price moved within one day.
  - range_ratio: normalizes the range relative to the opening price; a larger ratio = more volatile day.
``` python
df['daily_range'] = df['high'] - df['low']             # intraday spread
df['range_ratio'] = df['daily_range'] / df['open']     # relative daily volatility
```

# Measures market liquidity :
- how easy it is to buy/sell without big price change.
```
df['liquidity_ratio'] = df['volume'] / (df['market_cap'].replace({0: np.nan}).fillna(method='ffill').fillna(1))
```
# Technical Indicators — Bollinger Bands:
  -  Bollinger Bands = technical indicator that measures price volatility.

  - ma_20: 20-day moving average (the “middle band”).

  - std_20: 20-day rolling standard deviation.

  - bb_upper / bb_lower: upper and lower bands (±2 std).

   - bb_width: distance between bands → wide = more volatile, narrow = stable.
  ```
df['ma_20'] = df.groupby('crypto_name')['close'].rolling(window=20, min_periods=1).mean().reset_index(0, drop=True)
df['std_20'] = df.groupby('crypto_name')['close'].rolling(window=20, min_periods=1).std().reset_index(0, drop=True)
df['bb_upper'] = df['ma_20'] + 2 * df['std_20']
df['bb_lower'] = df['ma_20'] - 2 * df['std_20']
df['bb_width'] = df['bb_upper'] - df['bb_lower']
```
# Average True Range (ATR):
   - ATR = another volatility measure used in trading.

   - shift(1) gets the previous day’s closing price.

   -  Calculates three possible ranges:

      1. High-Low

      2. |High − Previous Close|

      3. |Low − Previous Close|

 - max(axis=1) takes the largest of the three = the True Range for that day.
 
 - rolling(window=14).mean() computes the 14-day average of True Range = ATR-14.
  - Larger ATR ⇒ higher volatility.

  ```
df['prev_close'] = df.groupby('crypto_name')['close'].shift(1)
df['tr1'] = df['high'] - df['low']
df['tr2'] = abs(df['high'] - df['prev_close'])
df['tr3'] = abs(df['low'] - df['prev_close'])
df['true_range'] = df[['tr1', 'tr2', 'tr3']].max(axis=1)
df['atr_14'] = df.groupby('crypto_name')['true_range'].rolling(window=14, min_periods=1).mean().reset_index(0, drop=True)
```

#  Terget Variable:
   - Goal: predict tomorrow’s volatility.
   - shift(-1) moves the vol_7 column one row up, so each row’s target corresponds to the next day’s 7-day volatility.
   -  This becomes our Y (dependent variable) for model training.
```
df['target_vol_7_next'] = df.groupby('crypto_name')['vol_7'].shift(-1)
```
# Relevant features for modeling:
```
feature_cols = [
    'open','high','low','close','volume','market_cap',
    'returns','vol_7','vol_30','ma_7','ma_30',
    'daily_range','range_ratio','liquidity_ratio',
    'bb_width','atr_14'
]
target_col = 'target_vol_7_next'
```
	​
