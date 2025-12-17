# webapp/file_utils.py

import os
import math
import magic  # pip install python-magic-bin (for Windows)

# 🔎 Entropy calculation

def calculate_entropy(data):
    if not data:
        return 0
    entropy = 0
    for x in range(256):
        p_x = data.count(bytes([x])) / len(data)
        if p_x > 0:
            entropy += - p_x * math.log2(p_x)
    return entropy

# 🔍 Feature extraction from file

def extract_file_features(filepath):
    try:
        with open(filepath, "rb") as f:
            raw = f.read()
            size = os.path.getsize(filepath)
            entropy = calculate_entropy(raw)
            file_type = magic.from_file(filepath)
            header = raw[:8].hex()  # first 8 bytes (magic header)

            return {
                "size": size,
                "entropy": entropy,
                "file_type": file_type,
                "header": header
            }
    except Exception as e:
        print(f"[Error] Feature extraction failed: {e}")
        return None
