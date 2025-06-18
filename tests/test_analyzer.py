import pytest
import pandas as pd
from data_analyzer import compute_statistics, detect_anomalies

# Sample DataFrame for testing
@pytest.fixture
def sample_df():
    data = {
        "timestamp": [
            "2025-06-15 12:00:00",
            "2025-06-15 12:00:01",
            "2025-06-15 12:00:02",
            "2025-06-15 12:00:03",
            "2025-06-15 12:00:04"
        ],
        "temperature": [24.8, 19.5, 31.2, 25.1, 28.7],
        "humidity": [48.2, 52.7, 65.0, 34.5, 50.1],
        "vibration": [0.021, 0.022, 0.041, 0.019, 0.017]
    }
    return pd.DataFrame(data)

def test_compute_statistics(sample_df):
    stats = compute_statistics(sample_df)
    assert isinstance(stats, pd.DataFrame)
    assert set(["mean", "min", "max", "std"]).issubset(stats.index)
    assert set(["temperature", "humidity", "vibration"]).issubset(stats.columns)

def test_detect_anomalies_structure(sample_df):
    thresholds = {
        "temperature": (20, 30),
        "humidity": (35, 70),
        "vibration": (0.005, 0.04)
    }
    anomalies = detect_anomalies(sample_df, thresholds)
    assert isinstance(anomalies, dict)
    for sensor, df in anomalies.items():
        assert isinstance(df, pd.DataFrame)
        assert set(["timestamp", "temperature", "humidity", "vibration"]).issubset(df.columns)

def test_detect_anomalies_counts(sample_df):
    thresholds = {
        "temperature": (20, 30),    # 19.5 and 31.2 are anomalies
        "humidity": (35, 70),       # 34.5 is an anomaly
        "vibration": (0.005, 0.04)  # 0.041 is an anomaly
    }
    anomalies = detect_anomalies(sample_df, thresholds)
    assert len(anomalies["temperature"]) == 2
    assert len(anomalies["humidity"]) == 1
    assert len(anomalies["vibration"]) == 1
