# Zenoh Real-time ECG Monitor | Advanced Computer Programming

Mochammad Naufal Ihza Syahzada - 112021223

A real-time ECG (Electrocardiogram) signal visualization system built with Eclipse Zenoh and Python. This project demonstrates real-time data publishing and visualization using simulated ECG signals.

## Features

- Real-time ECG signal generation using NeuroKit2
- Point-by-point data transmission at 200Hz sampling rate
- Live visualization with sliding time window
- Efficient publisher-subscriber architecture using Eclipse Zenoh
- Smooth real-time plotting with Matplotlib animation

## Requirements

- Python 3.7+
- Eclipse Zenoh
- NeuroKit2
- Matplotlib
- NumPy

## Installation

1. Clone the repository:
```bash
git clone https://github.com/NaufalIhza17/zenoh-realtime-ecg.git
cd zenoh-realtime-ecg
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the publisher (ECG signal generator):
```bash
python z_publisher.py
```

2. In a separate terminal, start the subscriber (visualization):
```bash
python z_subscriber.py
```

The subscriber will display a real-time plot of the ECG signal with a 5-second sliding window.

## Components

- `z_publisher.py`: Generates and publishes ECG signal data points
- `z_subscriber.py`: Receives data and creates real-time visualization
- `requirements.txt`: List of Python package dependencies

## Technical Details

- Sampling Rate: 200 Hz
- Display Window: 5 seconds
- Buffer Size: 1000 data points
- Plot Update Rate: 50ms (20 Hz)

## License

MIT License

## Acknowledgments

- [Eclipse Zenoh](https://zenoh.io/) for the pub/sub middleware
- [NeuroKit2](https://neurokit2.readthedocs.io/) for ECG signal simulation
- [Matplotlib](https://matplotlib.org/) for visualization 