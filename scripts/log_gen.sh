#!/bin/bash

# Create the data directory if it doesn't exist
mkdir -p ../data

LOG_FILE="../data/system_logs.csv"
echo "timestamp,cpu_usage,mem_usage,latency" > $LOG_FILE

echo "Starting log generation... Press [CTRL+C] to stop."

while true
do
  TIMESTAMP=$(date +%s)
  # Generate normal values (CPU 20-40%, Mem 30-50%, Latency 10-20ms)
  CPU=$(( ( RANDOM % 20 ) + 20 ))
  MEM=$(( ( RANDOM % 20 ) + 30 ))
  LATENCY=$(( ( RANDOM % 10 ) + 10 ))

  # Occasionally inject an anomaly (e.g., 5% chance)
  if [ $(( RANDOM % 20 )) -eq 0 ]; then
    CPU=$(( ( RANDOM % 40 ) + 60 )) # High CPU spike
    LATENCY=$(( ( RANDOM % 100 ) + 200 )) # High Latency
    echo "ANOMALY INJECTED: $TIMESTAMP"
  fi

  echo "$TIMESTAMP,$CPU,$MEM,$LATENCY" >> $LOG_FILE
  sleep 1 # Simulate 1 log per second
done