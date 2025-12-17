import pandas as pd

# Replace 'url.csv' with your actual filename if different
df = pd.read_csv("url.csv")

print("✅ Columns in the dataset:")
print(df.columns)
