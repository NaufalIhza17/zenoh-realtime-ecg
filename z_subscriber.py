import zenoh
import json
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import numpy as np

# Configure the plot settings
WINDOW_SIZE = 1000  # Number of points to display
data_buffer = deque(maxlen=WINDOW_SIZE)
time_buffer = deque(maxlen=WINDOW_SIZE)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 4))
line, = ax.plot([], [], 'b-', label='ECG Signal')
ax.set_title('Real-time ECG Signal')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
ax.grid(True)
ax.legend()

def listener(sample):
    try:
        # Parse the received JSON data
        data = json.loads(sample.payload.to_string())
        value = data["value"]
        timestamp = data["timestamp"]
        
        # Add new data to buffers
        data_buffer.append(value)
        time_buffer.append(timestamp)
        
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON data: {e}")
    except KeyError as e:
        print(f"Missing expected key in data: {e}")

def update_plot(frame):
    if len(data_buffer) > 0:
        # Convert timestamps to relative time (seconds from start)
        relative_times = np.array(time_buffer) - time_buffer[0]
        
        # Update the line data
        line.set_data(relative_times, data_buffer)
        
        # Adjust the plot limits
        ax.set_xlim(max(0, relative_times[-1] - 5), relative_times[-1] + 0.5)
        ax.set_ylim(min(data_buffer) - 0.1, max(data_buffer) + 0.1)
    
    return line,

if __name__ == "__main__":
    # Initialize Zenoh session
    session = zenoh.open(zenoh.Config())
    
    # Subscribe to ECG data
    sub = session.declare_subscriber('ecg/realtime', listener)
    
    try:
        # Set up the animation
        ani = animation.FuncAnimation(
            fig, update_plot, interval=50,  # Update every 50ms
            blit=True, cache_frame_data=False
        )
        
        # Show the plot (this blocks until window is closed)
        plt.show()
        
    except KeyboardInterrupt:
        print("Stopping subscriber...")
    finally:
        session.close()