import numpy as np
import matplotlib.pyplot as plt
import time
from collections import deque

plt.ion()
fig, ax = plt.subplots()

x_data = []
y_data = []
x_flagged = []
y_flagged = []
anomaly = []

window = deque(maxlen = 80)

sample_rate = 400

duration = 10

signal_freq = 5

amplitude = 1

numb_samples = sample_rate * duration

clock = np.linspace(0, duration, numb_samples, endpoint = False)


y = amplitude * np.sin(2 * np.pi * signal_freq * clock)



#sensors always have small random fluctuations in the way they read things
#Even though this happens doesn't mean an error occurred
#This noise makes the artificial sensor data act like real sensor data
noise = np.random.normal(0, .01, numb_samples)

sensor_reading = y + noise

# injected a spike anomaly

sensor_reading[3950:3999] += 2

anomaly_range = (3950, 3999)

#I made a for loop that will run through all the values throughout the sample characterizing a 400Hz signal
for i in range(numb_samples):
    window.append(sensor_reading[i])
    mean = np.mean(window)
    standardDeviation = np.std(window)
    x_data.append(clock[i])
    y_data.append(sensor_reading[i])
    
    if len(window) == window.maxlen:
        zscore = ((sensor_reading[i]-mean)/standardDeviation)
        if abs(zscore) > 3:
            x_flagged.append(clock[i])
            y_flagged.append(sensor_reading[i])
            
            print("anomaly detected at this index" , i)
            anomaly.append(i)
    if i % 20 == 0:
        ax.clear()
        ax.plot(x_data, y_data)
        ax.plot(x_flagged, y_flagged, 'ro')
        plt.pause(1/sample_rate)
    
#Finding anomalies
true_anomalies = set(range(anomaly_range[0], anomaly_range[1] + 1))
detected = set(anomaly)

missed = true_anomalies - detected
false_positives = detected - true_anomalies

print("Missed:", missed)
print("False positives:", false_positives)   

#Will replace sensor_reading[i] with get_serial_sample once connected to MPU6050
def get_synthetic_sample():
    global i
    sample = sensor_reading[i]
    i += 1
    return sample

def get_serial_sample():
    line = arduino_serial.readline()
    return float(line)






