import pandas as pd
from sklearn.ensemble import IsolationForest
import time
import os

LOG_FILE = "data/system_logs.csv"


def get_latest_data(n=100):
    """Reads the last n lines from the log file."""
    if not os.path.exists(LOG_FILE):
        return None
    df = pd.read_csv(LOG_FILE)
    return df.tail(n)


def monitor_stream():
    # Initialize Model
    model = IsolationForest(contamination=0.05)  # Expect 5% anomalies

    print("Monitoring stream...")
    while True:
        df = get_latest_data(100)
        if df is not None and len(df) > 10:
            # Features: CPU, Mem, Latency
            features = df[['cpu_usage', 'mem_usage', 'latency']]

            # Fit and Predict
            model.fit(features)
            df['anomaly'] = model.predict(features)

            # -1 indicates an anomaly in Isolation Forest
            latest_status = df.iloc[-1]
            if latest_status['anomaly'] == -1:
                print(f"⚠️ ANOMALY DETECTED at {latest_status['timestamp']}")

        time.sleep(2)


if __name__ == "__main__":
    monitor_stream()