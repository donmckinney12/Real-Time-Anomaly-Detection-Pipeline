# Real-Time Streaming Anomaly Detection Pipeline

## Overview
An end-to-end MLOps pipeline that monitors system health logs in real-time. It uses a Linux-based data producer and an Isolation Forest model to detect performance anomalies.

## Tech Stack
- **Language:** Python 3.x, Shell Scripting (Bash)
- **ML:** Scikit-Learn (Isolation Forest)
- **Backend:** Flask
- **Data:** Simulated real-time system logs (CPU, Memory, Latency)

## Architecture
1. **Producer:** Bash script simulating live server metrics.
2. **Detector:** Python engine using a sliding window for real-time inference.
3. **Dashboard:** Flask UI to visualize anomalies (Coming Soon).
