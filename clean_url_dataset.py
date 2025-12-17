import pandas as pd

# Load full dataset
df = pd.read_csv("url.csv", low_memory=False)

# Check for required columns
if "url" in df.columns and "class" in df.columns:
    df_clean = df[["url", "class"]]  # Keep only URL and label
    df_clean = df_clean.dropna()     # Drop any rows with missing values
    df_clean.to_csv("clean_url.csv", index=False)
    print(f"✅ Saved cleaned dataset with {len(df_clean)} rows to 'clean_url.csv'")
else:
    print("❌ 'url' or 'class' column not found in dataset.")
