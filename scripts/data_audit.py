import pandas as pd

df = pd.read_csv('../data/Global_Superstore2.csv', encoding='latin1')

print(f"Rows: {len(df):,} | Columns: {len(df.columns)}")
print("\nMissing values:")
print(df.isnull().sum()[df.isnull().sum() > 0])
print(f"\nDuplicate rows: {df.duplicated().sum()}")
print(f"\nDate sample: {df['Order Date'].head(3).tolist()}")
print(f"\nProfit range: ${df['Profit'].min():,.2f} to ${df['Profit'].max():,.2f}")
print("\nData types:")
print(df.dtypes)