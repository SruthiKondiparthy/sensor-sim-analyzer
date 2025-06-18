import pandas as pd

def load_data(file_path="data/simulated_data.csv"):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def compute_statistics(df):
    stats = df.describe().loc[["mean", "min", "max", "std"]]
    return stats

def detect_anomalies(df, thresholds):
    anomalies = {}

    for column, (min_val, max_val) in thresholds.items():
        mask = ~df[column].between(min_val, max_val)
        anomalies[column] = df[mask]

    return anomalies

def print_report(stats, anomalies):
    print("\n=== Sensor Statistics ===")
    print(stats)

    print("\n=== Anomalies Detected ===")
    for sensor, rows in anomalies.items():
        print(f"\n{sensor.upper()} anomalies: {len(rows)}")
        if not rows.empty:
            print(rows.head(3).to_string(index=False))  # Show a few examples

if __name__ == "__main__":
    df = load_data()
    if df is not None:
        stats = compute_statistics(df)
        thresholds = {
            "temperature": (20, 30),
            "humidity": (35, 70),
            "vibration": (0.005, 0.04)
        }
        anomalies = detect_anomalies(df, thresholds)
        print_report(stats, anomalies)
