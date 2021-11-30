import matplotlib.pyplot as plt
import serial
import threading

ser = serial.Serial('COM3', 115200, timeout=5)
data_list = []
content = ""

while True:
    content = str(ser.readline())
