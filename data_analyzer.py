import pytest
import pandas as pd
from sensor_simulator import generate_sensor_data

def test_return_type():
    df = generate_sensor_data(num_samples=10)
    assert isinstance(df, pd.DataFrame), "Output should be a DataFrame"

def test_dataframe_columns():
    df = generate_sensor_data(num_samples=10)
    expected_cols = ["timestamp", "temperature", "humidity", "vibration"]
    assert list(df.columns) == expected_cols, f"Expected columns {expected_cols}, got {list(df.columns)}"

def test_row_count():
    num_samples = 50
    df = generate_sensor_data(num_samples=num_samples)
    assert len(df) == num_samples, f"Expected {num_samples} rows, got {len(df)}"

def test_temperature_range():
    df = generate_sensor_data(num_samples=1000, anomaly_rate=0)  # No anomalies
    outliers = df[~df['temperature'].between(20, 30)]
    assert len(outliers) / len(df) < 0.05, f"Too many out-of-range temperatures: {len(outliers)} out of {len(df)}"

def test_vibration_range():
    df = generate_sensor_data(num_samples=1000, anomaly_rate=0)  # No anomalies
    outliers = df[~df['vibration'].between(0.005, 0.04)]
    assert len(outliers) / len(df) < 0.05, f"Too many out-of-range vibration values: {len(outliers)} out of {len(df)}"
