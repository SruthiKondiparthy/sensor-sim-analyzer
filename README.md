📊 Sensor Data Simulator & Analyzer
A Python-based tool to simulate, analyze, and optionally visualize sensor data for testing industrial, IoT, or embedded system workflows.

🎯 Project Aim
This project generates realistic time-series sensor data (temperature, humidity, and vibration) with optional anomaly injection. It is designed to support:
    Data science workflows
    Anomaly detection system testing
    Embedded software validation
    Monitoring dashboards and simulations

🧠 Features
✅ Simulates 3 sensor types:
    Temperature (°C)
    Humidity (%)
    Vibration (g or arbitrary units)

✅ Supports:
    Realistic random noise (using normal distribution)
    Configurable number of data points
    Optional anomaly injection (e.g. spikes, abnormal vibration)

✅ Outputs:
    Structured CSV file with timestamps
    Easy to plug into pandas, Excel, or dashboards

🛠 Technology Stack
    Python 3.x
    pandas, numpy for data generation
    matplotlib or plotly (for optional visualization)
    pytest for testing

🧪 Example Output
timestamp	temperature	humidity	vibration
2025-06-15 12:00:00	24.6	52.1	0.0215
2025-06-15 12:00:01	25.2	49.3	0.0198

🚀 How to Run
    Install dependencies
    (optional: create a virtual environment first)

pip install -r requirements.txt

Generate data
    python sensor_simulator.py
    Output will be saved to: data/simulated_data.csv

🔬 How to Run Tests
Run unit tests using pytest:
pytest tests/

Tests include:
    Data structure and format checks
    Range validation (including anomaly-free mode)
