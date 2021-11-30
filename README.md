# safe-drive
Safe Drive project that implements Drowsiness Detection along with inertial sensor reading and inference. Other codes are also available, like plotting data, statistics calculation and others.

All the functionalities were implemented on a NVIDIA Jetson Nano for real time inference. The list of hardware is listed bellow:
- NVIDIA Jetson Nano
- Picamera V2
- MPU6050 (triple axis accelerometer and gyroscope)
- ublox NEO 6M-V2 GPS

The full code can be checked in the drowsiness.py file.

Note: The Drowsiness Detection functionality was based on DBSE-monitor project that was posted on GitHub (https://github.com/altaga/DBSE-monitor).
