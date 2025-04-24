import pandas as pd
import numpy as np
import os
import json
from datetime import datetime

# -------------------------------------------
# Function: Save metrics as JSON
# -------------------------------------------
def save_metrics(metrics: dict, output_path: str = "models/metrics.json"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(metrics, f, indent=4)
    print(f"[INFO] Metrics saved to {output_path}")

# -------------------------------------------
# Function: Timestamp logger
# -------------------------------------------
def log(message: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

# -------------------------------------------
# Function: Display basic dataset summary
# -------------------------------------------
def summarize_dataset(df: pd.DataFrame):
    print("🔍 Dataset Summary:")
    print(f"Shape: {df.shape}")
    print("\nMissing Values:\n", df.isnull().sum())
    print("\nData Types:\n", df.dtypes)
    print("\nStatistical Overview:\n", df.describe())