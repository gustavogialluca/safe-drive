import serial
import pynmea2
import geopy.distance
import time

ser = serial.Serial('COM3', 115200, timeout=5)
gps_list = []
delta_t = 0
time_since_last_read = 0
velocity_list = []

start = time.time()

while True:
    content = str(ser.readline())
    if content.startswith('b\'$GPGGA'):
        print(content)
        stop = time.time()
        delta_t = stop - start
        start = time.time()
        try:
            gps_content = content.split('\'')[1].split('\\')[0]
            msg = pynmea2.parse(gps_content)
            response = repr(msg.latitude) + "," + repr(msg.longitude)
            if response != "0.0,0.0":
                lat, lng = response.split(',')
                # print(float(lat), float(lng))
                gps_list.append((float(lat), float(lng)))
                # print(gps_list)
            # print(delta_t)
        except pynmea2.ParseError as e:
            print('Parse error: {}'.format(e))
            continue
        if len(gps_list) > 1:
            # print(gps_list)
            coord_1 = gps_list[-1]
            coord_2 = gps_list[-2]
            V_m_s = geopy.distance.distance(coord_1, coord_2).m / delta_t
            V_km_h = V_m_s * 3.6
            velocity_list.append(V_km_h)
            print("#######################################")
            print("V (m/s) = " + str(V_m_s) + str(' m/s'))
            print("V (km/h) = " + str(V_km_h) + str(' km/h'))
            print("#######################################")
            print()
            if len(velocity_list) >= 2:
                print("[2 SECONDS]: " + str((velocity_list[-1] + velocity_list[-2]) / 2))
            if len(velocity_list) >= 5:
                print("[5 SECONDS]:" + str((velocity_list[-1] + velocity_list[-2] + velocity_list[-3] + velocity_list[-4] + velocity_list[-5]) / 5))
            if len(velocity_list) >= 10:
                print("[10 SECONDS]:" + str((velocity_list[-1] + velocity_list[-2] + velocity_list[-3] + velocity_list[-4] + velocity_list[-5] +
                                        velocity_list[-6] + velocity_list[-7] + velocity_list[-8] + velocity_list[-9] + velocity_list[-10]) / 10))