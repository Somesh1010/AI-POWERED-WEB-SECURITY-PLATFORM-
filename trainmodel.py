# train_model.py

import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
import joblib

# Step 1: Create sample data (or replace with real extracted flow data)
# Features: [packet_length, protocol]
data = {
    "length": [60, 70, 65, 100, 500, 200, 3000, 8000, 12000, 90, 75, 82, 110, 10500],
    "protocol": ["TCP", "TCP", "UDP", "TCP", "UDP", "TCP", "UDP", "TCP", "UDP", "UDP", "TCP", "TCP", "UDP", "TCP"]
}

df = pd.DataFrame(data)

# Step 2: Encode protocol
le = LabelEncoder()
df["protocol_encoded"] = le.fit_transform(df["protocol"])

# Step 3: Train Isolation Forest (Unsupervised Anomaly Detection)
model = IsolationForest(contamination=0.2, random_state=42)
model.fit(df[["length", "protocol_encoded"]])

# Step 4: Save model
joblib.dump(model, "ml_model.pkl")

print("✅ Model trained and saved as ml_model.pkl")
