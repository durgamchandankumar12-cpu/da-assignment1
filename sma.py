import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/AAPL.csv")

print("Columns:", df.columns)
print(df.head())

# 🔥 Clean column properly
df['Round Lot Size'] = df['Round Lot Size'].replace(' ', None)
df['Round Lot Size'] = pd.to_numeric(df['Round Lot Size'], errors='coerce')

# 🔥 Drop only rows where this column is NaN
df = df[df['Round Lot Size'].notna()]

print("After cleaning:", df.shape)

# ✅ Apply SMA
df['SMA'] = df['Round Lot Size'].rolling(5).mean()

print(df[['Round Lot Size','SMA']].head())

# ✅ Plot
df[['Round Lot Size','SMA']].head(50).plot(title="SMA on Round Lot Size")
plt.show()