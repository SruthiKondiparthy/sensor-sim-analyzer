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
    df = generate_sensor_data(num_samples=100, anomaly_rate=0)  # No anomalies
    assert df['temperature'].between(20, 30).all(), "Temperatures should be in 20–30°C range (± noise)"

def test_vibration_range():
    df = generate_sensor_data(num_samples=100, anomaly_rate=0)  # No anomalies
    assert df['vibration'].between(0.01, 0.03).all(), "Vibration values should be in 0.01–0.03 range"
