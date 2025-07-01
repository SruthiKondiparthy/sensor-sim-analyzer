"""
✅ Sidebar controls
✅ Live Data Simulation toggle
✅ CSV download button
✅ Tabbed visualizations for each sensor
✅ Anomaly detection & stats reporting
"""


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
import io
from sensor_simulator import generate_sensor_data
from data_analyzer import compute_statistics, detect_anomalies

# App title
st.title("📊 Sensor Data Simulator & Analyzer")

# Sidebar controls
st.sidebar.header("🔧 Settings")
num_samples = st.sidebar.slider("Number of Samples", 10, 1000, 100)
anomaly_rate = st.sidebar.slider("Anomaly Rate", 0.0, 0.3, 0.05, step=0.01)

# Live simulation toggle
st.sidebar.markdown("---")
live_mode = st.sidebar.checkbox("📡 Live Data Simulation", value=False)

# Main content
st.subheader("1. Simulated Sensor Data")

if live_mode:
    st.info("Live Mode Active — Generating 1 sample per second...")
    live_df = pd.DataFrame(columns=["timestamp", "temperature", "humidity", "vibration"])
    placeholder = st.empty()

    for i in range(num_samples):
        new_row = generate_sensor_data(num_samples=1, anomaly_rate=anomaly_rate)
        live_df = pd.concat([live_df, new_row], ignore_index=True)

        placeholder.dataframe(live_df.tail(10))  # Show latest 10 readings
        time.sleep(1)
    df = live_df  # Use for analysis below
else:
    df = generate_sensor_data(num_samples=num_samples, anomaly_rate=anomaly_rate)
    st.write(df.head())

# Download CSV button
csv_data = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="⬇️ Download CSV",
    data=csv_data,
    file_name="simulated_data.csv",
    mime="text/csv"
)

# Thresholds for anomaly detection
thresholds = {
    "temperature": (20, 30),
    "humidity": (35, 70),
    "vibration": (0.005, 0.04)
}

# Compute stats
st.subheader("2. Sensor Statistics")
stats = compute_statistics(df)
st.dataframe(stats)

# Detect anomalies
st.subheader("3. Anomaly Detection")
anomalies = detect_anomalies(df, thresholds)
for sensor, rows in anomalies.items():
    st.write(f"**{sensor.capitalize()} anomalies**: {len(rows)}")
    if not rows.empty:
        st.dataframe(rows.head())

# Visualization tabs
st.subheader("4. Visualize Sensor Data")

tabs = st.tabs(["🌡 Temperature", "💧 Humidity", "🌀 Vibration"])
sensor_names = ["temperature", "humidity", "vibration"]

for i, sensor in enumerate(sensor_names):
    with tabs[i]:
        time_series = pd.to_datetime(df["timestamp"])
        values = df[sensor]
        mask = ~values.between(thresholds[sensor][0], thresholds[sensor][1])
        anomalies_df = df[mask]

        fig, ax = plt.subplots(figsize=(10, 3))
        ax.plot(time_series, values, label=sensor.capitalize(), color='blue')
        ax.scatter(pd.to_datetime(anomalies_df["timestamp"]), anomalies_df[sensor], color='red', label='Anomalies')
        ax.set_title(f"{sensor.capitalize()} Over Time")
        ax.set_xlabel("Time")
        ax.set_ylabel(sensor.capitalize())
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)


