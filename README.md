# 1-DOF PID Test Rig & Telemetry Anomaly Visualizer

A Python-based data pipeline and physical test rig architecture designed to ingest, visualize, and analyze high-frequency sensor telemetry (400Hz) for flight stabilization loops. 

## Project Overview
Before deploying control algorithms to an autonomous quadcopter, they must be validated against hardware anomalies. This project features a continuous rolling window algorithm to calculate statistical baselines (mean and standard deviation) on the fly. By applying a real-time z-score threshold, the system instantly flags sudden signal deviations caused by unexpected mechanical vibrations, sensor drift, or hardware voltage drops.

## Features
* **Real-Time Visualization:** Uses `matplotlib.pyplot` to dynamically graph the telemetry stream and overlay flagged anomalies as they occur.
* **Rolling Z-Score Detection:** Implements a sliding window (`collections.deque`) to dynamically adjust to changing baselines, preventing false positives during intentional altitude or pitch changes.
* **Hardware-in-the-Loop Ready:** Currently configured with a synthetic 400Hz NumPy data generator with injected Gaussian noise and transient spikes. Built with modular functions to seamlessly swap to live `pyserial` ingestion from an Arduino/ESP32 handling an MPU6050 6-axis IMU.
* **Performance Metrics:** Automatically calculates false positive and missed detection rates against known injected anomalies to tune the Z-score threshold.

## Tech Stack
* **Language:** Python 3, C++ (Arduino/ESP32)
* **Libraries:** NumPy, Matplotlib, Pandas
* **Hardware:** MPU6050 IMU, Custom 3D-printed 1-DOF seesaw pivot with low-stiction 608 bearings

## Getting Started
1. Clone this repository.
2. Install dependencies: `pip install numpy matplotlib`
3. Run the visualizer: `python anomaly_visualizer.py`