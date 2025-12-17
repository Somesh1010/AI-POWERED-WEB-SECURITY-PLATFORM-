import pyshark
import pandas as pd
import joblib
import asyncio

# 🧠 Ensure Flask thread has an event loop for pyshark
def ensure_event_loop():
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

# 📦 Load your trained ML model (Isolation Forest)
model = joblib.load("ml_model.pkl")

# 🧬 Feature extractor for each packet
def extract_features(packet):
    try:
        return {
            "protocol": packet.highest_layer,
            "length": int(packet.length),
            "src": packet.ip.src,
            "dst": packet.ip.dst
        }
    except:
        return None

# 📡 Analyze live network traffic using pyshark + ML
def analyze_live_traffic(limit=50):
    ensure_event_loop()

    # 🔁 Interface name may need to be changed (e.g., 'Ethernet' or 'eth0')
    cap = pyshark.LiveCapture(interface='Wi-Fi')
    features = []

    print("📡 Capturing packets...")

    for packet in cap.sniff_continuously(packet_count=limit):
        data = extract_features(packet)
        if data:
            features.append(data)

    # 🧪 Prepare features for model
    df = pd.DataFrame(features)
    df["length"] = pd.to_numeric(df["length"], errors='coerce').fillna(0)
    df["protocol_encoded"] = df["protocol"].astype("category").cat.codes

    # 🤖 Predict anomalies
    predictions = model.predict(df[["length", "protocol_encoded"]])
    df["anomaly"] = predictions

    # 🔍 Filter only anomalous flows
    anomalies = df[df["anomaly"] == -1]
    return anomalies.to_dict(orient="records")
"""
import pyshark
import pandas as pd
import joblib
import asyncio

# 🧠 Ensure Flask thread has an event loop for pyshark
def ensure_event_loop():
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

# 📦 Load your trained ML model (Isolation Forest)
model = joblib.load("ml_model.pkl")

# 🧬 Extract basic features from a packet
def extract_features(packet):
    try:
        return {
            "protocol": packet.highest_layer,
            "length": int(packet.length),
            "src": packet.ip.src,
            "dst": packet.ip.dst
        }
    except:
        return None

# 📂 Analyze packets from uploaded PCAP file
def analyze_live_traffic(limit=50):
    ensure_event_loop()

    cap = pyshark.FileCapture("2025-06-13-traffic-analysis-exercise.pcap", keep_packets=False)
    features = []

    print("📡 Reading from PCAP file...")

    for i, packet in enumerate(cap):
        if i >= limit:
            break
        data = extract_features(packet)
        if data:
            features.append(data)

    cap.close()

    # 🧪 Prepare feature dataframe
    df = pd.DataFrame(features)
    df["length"] = pd.to_numeric(df["length"], errors='coerce').fillna(0)
    df["protocol_encoded"] = df["protocol"].astype("category").cat.codes

    # 🤖 Predict using ML model
    predictions = model.predict(df[["length", "protocol_encoded"]])
    df["anomaly"] = predictions

    # 🔍 Filter only anomalies
    anomalies = df[df["anomaly"] == -1]
    return anomalies.to_dict(orient="records")"""
