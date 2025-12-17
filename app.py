from flask import Flask, render_template, request, jsonify
import os
import joblib
from werkzeug.utils import secure_filename

from file_utils import extract_file_features             # ✅ Module 3 - File feature extraction
from network_monitor import analyze_live_traffic         # ✅ Module 2 - Network anomaly detection
from feature_extractor import FeatureExtractor           # ✅ Module 1 - Feature extractor (109-feature version)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# 🚀 Load trained ML models
url_model = joblib.load("url_model.pkl")                 # ✅ Module 1 - URL classifier model
file_model = joblib.load("malware_model.pkl")            # ✅ Module 3 - Malware classifier model

# 🌐 Home Page
@app.route("/")
def home():
    return render_template("index.html")

# 🔗 Module 1: URL Scan using 109 features (ML Only)
@app.route("/scan", methods=["POST"])
def scan_url():
    url = request.json.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        extractor = FeatureExtractor()
        features = extractor.extract_features(url)

        # 🐛 Debug print: show how many features are being passed
        print(f"[DEBUG] Extracted {len(features)} features")
        print(f"[DEBUG] Feature keys: {list(features.keys())}")

        if features is None or len(features) != 108:
            return jsonify({"error": f"Feature extraction failed or incorrect number of features: {len(features)}"}), 500

        prediction = url_model.predict([list(features.values())])[0]
        result = "Malicious" if prediction == 1 else "Safe"

        return jsonify({
            "status": result,
            "url": url,
            "features_used": features
        })

    except Exception as e:
        print("❌ URL Scan Error:", e)
        return jsonify({"error": str(e)}), 500
'''
@app.route("/scan", methods=["POST"])
def scan_url():
    url = request.json.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        extractor = FeatureExtractor()
        features = extractor.extract_features(url)  # ✅ Correct method name

        if features is None or len(features) != 109:
            return jsonify({"error": "Feature extraction failed or incorrect number of features"}), 500

        prediction = url_model.predict([list(features.values())])[0]
        result = "Malicious" if prediction == 1 else "Safe"

        return jsonify({
            "status": result,
            "url": url,
            "features_used": features
        })

    except Exception as e:
        print("❌ URL Scan Error:", e)
        return jsonify({"error": str(e)}), 500
'''
# 📡 Module 2: Network Traffic Anomaly Detection
@app.route("/analyze-traffic", methods=["GET"])
def analyze_traffic():
    try:
        anomalies = analyze_live_traffic(limit=50)
        return jsonify({"anomalies": anomalies, "count": len(anomalies)})
    except Exception as e:
        print("❌ Traffic Analysis Error:", e)
        return jsonify({"error": str(e)}), 500

# 🔢 Module 3: File Malware Detection
@app.route("/scan-file", methods=["POST"])
def scan_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    try:
        features = extract_file_features(filepath)
        if features is None:
            return jsonify({"error": "Failed to extract features"}), 500

        file_type_encoded = hash(features['file_type']) % 1000
        input_vector = [[features['size'], features['entropy'], file_type_encoded]]

        prediction = file_model.predict(input_vector)[0]
        result = "Malicious" if prediction == 1 else "Safe"

        return jsonify({
            "filename": filename,
            "status": result,
            "details": features
        })

    except Exception as e:
        print("❌ File Scan Error:", e)
        return jsonify({"error": str(e)}), 500

# 🚀 Start the Flask Server
if __name__ == "__main__":
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    app.run(debug=True)
