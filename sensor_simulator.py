"""We'll generate time-series data for 3 sensors:
    Temperature (°C)
    Humidity (%)
    Vibration (arbitrary units)
Each row will include a timestamp and values."""

import pandas as pd
import numpy as np
import datetime
import random
import os

def generate_sensor_data(num_samples=1000, anomaly_rate=0.05):
    data = []
    current_time = datetime.datetime.now()

    for _ in range(num_samples):
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
        
        # Normal ranges
        temp = np.random.normal(loc=25, scale=2)        # 25°C ± 2
        humidity = np.random.normal(loc=50, scale=5)    # 50% ± 5
        vibration = np.random.normal(loc=0.02, scale=0.005)  # small g-force variation

        # Inject anomalies occasionally
        if random.random() < anomaly_rate:
            temp += np.random.normal(15, 5)    # Sudden spike
            vibration += np.random.normal(0.1, 0.03)

        data.append([timestamp, round(temp, 2), round(humidity, 2), round(vibration, 4)])
        current_time += datetime.timedelta(seconds=1)

    df = pd.DataFrame(data, columns=["timestamp", "temperature", "humidity", "vibration"])
    return df

def save_data(df, filename="data/simulated_data.csv"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    df = generate_sensor_data()
    save_data(df)

