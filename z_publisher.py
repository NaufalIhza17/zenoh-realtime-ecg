import zenoh
import neurokit2 as nk
import time
import json
import numpy as np

def generate_ecg_data():
    # Generate 8 seconds of ECG data at 200Hz sampling rate with heart rate of 80 BPM
    ecg_signal = nk.ecg_simulate(duration=8, sampling_rate=200, heart_rate=80)
    return ecg_signal.tolist()  # Convert numpy array to list for JSON serialization

if __name__ == "__main__":
    # Initialize Zenoh session
    session = zenoh.open(zenoh.Config())
    publisher = session.declare_publisher("ecg/realtime")

    # Configuration
    sampling_rate = 200  # Hz
    delay = 1.0 / sampling_rate  # Time between data points

    try:
        current_data = []
        data_index = 0
        
        while True:
            # Generate new ECG data if needed
            if not current_data or data_index >= len(current_data):
                current_data = generate_ecg_data()
                data_index = 0
                print("Generated new ECG signal")
            
            # Get current data point
            value = current_data[data_index]
            timestamp = time.time()
            
            # Create data packet
            data = {
                "timestamp": timestamp,
                "value": value
            }
            
            # Publish the data point
            publisher.put(json.dumps(data))
            
            # Move to next data point
            data_index += 1
            
            # Wait for next sample time
            time.sleep(delay)
            
    except KeyboardInterrupt:
        print("Stopping publisher...")
    finally:
        session.close() 