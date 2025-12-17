# test_file_utils.py

from file_utils import extract_file_features

# Change this path to any actual file in your system for testing
file_path = "sample.pdf"  # <-- put a real file here (PDF, JPG, EXE, etc.)

features = extract_file_features(file_path)
print(features)
