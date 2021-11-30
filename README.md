# safe-drive
The main idea of this project is to avoid and detect drowsiness in vehicles, based on Drowsiness Detection via image processing and alerts generation via inertial sensors (accelerometer and gyroscope). All the processing uses machine learning techniques for real time inference.

The full code can be checked in the final.py file. Other codes are also available, like plotting data, statistics calculation, GPS nmea readings and others.

All the functionalities were implemented on a NVIDIA Jetson Nano for real time inference. The list of hardware is listed bellow:
- NVIDIA Jetson Nano
- Picamera V2
- MPU6050 (triple axis accelerometer and gyroscope)
- ublox NEO 6M-V2 GPS

Note: The Drowsiness Detection functionality was based on DBSE-monitor project that was posted on GitHub (https://github.com/altaga/DBSE-monitor).
