# Real-Time Streaming Anomaly Detection Pipeline

## 🚀 Project Overview
This project is a real-time monitoring system designed to detect system performance anomalies as they happen. It features a custom-built data producer, an unsupervised machine learning engine, and a live-updating web dashboard.

## 🛠️ Tech Stack
- **Languages:** Python 3.11, Bash
- **ML Framework:** Scikit-Learn (Isolation Forest)
- **Backend:** Flask (RESTful API)
- **Frontend:** HTML5, CSS3, Chart.js
- **DevOps:** Docker, Docker Compose

## 🏗️ Architecture
1. **Producer:** A multi-threaded Python generator simulating high-velocity system logs (CPU, Memory, Latency).
2. **ML Engine:** An Isolation Forest model that standardizes incoming data and performs unsupervised anomaly detection on a sliding window of the latest 50 events.
3. **Dashboard:** A real-time UI that polls the backend API every 2 seconds to visualize system health.

## 📦 Installation & Setup
1. **Clone the Repo:**
   `git clone https://github.com/YOUR_USERNAME/real-time-anomaly-detection.git`
2. **Launch with Docker:**
   `docker-compose up --build`
3. **Access Dashboard:** Navigate to `http://localhost:5000`