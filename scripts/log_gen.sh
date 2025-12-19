#!/bin/bash

# Force the directory to exist inside the container
mkdir -p /app/data
LOG_FILE="/app/data/system_logs.csv"

# If file doesn't exist, create it with headers
if [ ! -f "$LOG_FILE" ]; then
    echo "timestamp,cpu_usage,mem_usage,latency" > "$LOG_FILE"
fi

echo "Log generation started at $LOG_FILE"

while true
do
  # ... (your existing logic for TIMESTAMP, CPU, etc.)
  echo "$TIMESTAMP,$CPU,$MEM,$LATENCY" >> "$LOG_FILE"
  sleep 1
done