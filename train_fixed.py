import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.utils.class_weight import compute_class_weight
import numpy as np

# Load the CSV (features already extracted)
df = pd.read_csv("url.csv", low_memory=False)

# Split into features and labels
X = df.drop("class", axis=1)
y = df["class"]

# Compute class weights to handle imbalance
class_weights = compute_class_weight(class_weight="balanced", classes=np.unique(y), y=y)
weights_dict = {cls: weight for cls, weight in zip(np.unique(y), class_weights)}

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model with class weights
model = RandomForestClassifier(n_estimators=100, class_weight=weights_dict, random_state=42)
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
print("✅ Accuracy:", accuracy_score(y_test, preds))
print("✅ Report:\n", classification_report(y_test, preds))

# Save the model
joblib.dump(model, "url_model.pkl")
print("✅ Model saved as url_model.pkl")
