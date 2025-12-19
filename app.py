from flask import Flask, render_template, jsonify
import pandas as pd
import numpy as np
import os
import time
import threading
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
LOG_FILE = "/app/data/system_logs.csv"
model = IsolationForest(contamination=0.05)
scaler = StandardScaler()


# --- BACKGROUND DATA GENERATOR ---
def generate_data():
    """Generates logs directly from Python to avoid path issues."""
    os.makedirs("/app/data", exist_ok=True)
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w') as f:
            f.write("timestamp,cpu_usage,mem_usage,latency\n")

    while True:
        timestamp = int(time.time())
        # Normal data
        cpu = np.random.randint(20, 40)
        mem = np.random.randint(30, 50)
        lat = np.random.randint(10, 20)

        # 5% chance of anomaly
        if np.random.random() > 0.95:
            cpu = np.random.randint(80, 100)
            lat = np.random.randint(200, 300)

        with open(LOG_FILE, 'a') as f:
            f.write(f"{timestamp},{cpu},{mem},{lat}\n")
        time.sleep(1)


# Start generator in a background thread
threading.Thread(target=generate_data, daemon=True).start()


# --- ANALYTICS LOGIC ---
def detect_anomalies():
    if not os.path.exists(LOG_FILE):
        return []
    try:
        df = pd.read_csv(LOG_FILE)
        if len(df) < 2: return []

        window = df.tail(50).copy()
        features = ['cpu_usage', 'mem_usage', 'latency']

        if len(window) > 10:
            scaled = scaler.fit_transform(window[features])
            window['anomaly'] = model.fit_predict(scaled)
        else:
            window['anomaly'] = 1

        return window.to_dict(orient='records')
    except Exception as e:
        return []


# --- ROUTES ---
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/data')
def get_data():
    return jsonify(detect_anomalies())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)  # Disable debug for threads