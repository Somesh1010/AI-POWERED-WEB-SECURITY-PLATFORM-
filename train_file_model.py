# webapp/train_file_model.py

import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from file_utils import extract_file_features

# 📂 Set dataset paths
data_dir = "dataset"
classes = {"benign": 0, "malware": 1}

X = []  # Features
y = []  # Labels

# ▶️ Load all files and extract features
for label_name, label_val in classes.items():
    folder = os.path.join(data_dir, label_name)
    if not os.path.isdir(folder):
        continue

    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        features = extract_file_features(filepath)
        if features:
            X.append(features)
            y.append(label_val)

# ✅ Convert to DataFrame
df = pd.DataFrame(X)
df["label"] = y

# 🔹 Preprocess categorical features
df["file_type_encoded"] = df["file_type"].astype("category").cat.codes

# 🤖 Select final features for training
feature_cols = ["size", "entropy", "file_type_encoded"]
X_final = df[feature_cols]
y_final = df["label"]

# 🧠 Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_final, y_final)

# 🔢 Save model
joblib.dump(model, "malware_model.pkl")

print("🌟 Model trained and saved as malware_model.pkl")
