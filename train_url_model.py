import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils.class_weight import compute_class_weight
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from feature_extractor import FeatureExtractor

# Step 1: Load CSV
df = pd.read_csv("url.csv", low_memory=False)

# Step 2: Ensure the label exists
if 'class' not in df.columns:
    raise ValueError("The 'class' column is missing in your dataset.")

# Step 3: Extract features
extractor = FeatureExtractor()
X = []
y = []

for index, row in df.iterrows():
    try:
        url = str(row.get("url", ""))  # Gracefully handle missing 'url'
        label = int(row["class"])
        features = extractor.extract_features(url)
        X.append(list(features.values()))
        y.append(label)
    except Exception as e:
        print(f"⚠️ Skipping row {index} due to error: {e}")

print(f"🔍 Features shape: ({len(X)}, {len(X[0])})")

# Step 4: Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Compute class weights
class_weights = compute_class_weight(class_weight='balanced', classes=np.unique(y_train), y=y_train)
weights_dict = {cls: weight for cls, weight in zip(np.unique(y_train), class_weights)}

# Step 6: Train model with class weights
model = RandomForestClassifier(n_estimators=100, class_weight=weights_dict, random_state=42)
model.fit(X_train, y_train)

# Step 7: Evaluate
preds = model.predict(X_test)
print("✅ Accuracy:", accuracy_score(y_test, preds))
print("✅ Report:\n", classification_report(y_test, preds, zero_division=0))

# Step 8: Save model
joblib.dump(model, "url_model.pkl")
print("✅ Saved url_model.pkl")
