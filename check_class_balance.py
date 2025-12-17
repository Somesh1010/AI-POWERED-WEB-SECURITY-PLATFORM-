import pandas as pd
df = pd.read_csv("url.csv")
print(df['class'].value_counts())
