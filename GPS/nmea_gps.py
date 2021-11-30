import pynmea2

file = open('E:\\Gustavo\\GENERA\Direção Segura\\GPS\dados\\1_casa_gramado_cemiterio.txt', encoding='utf-8')
file_final  = open("gps_lat_long.txt", "w+")

for line in file.readlines():
    if line.startswith("$GPGGA"):
        try:
            msg = pynmea2.parse(line)
            response = repr(msg.latitude) + "," + repr(msg.longitude)
            if response != "0.0,0.0":
                print(response)
                file_final.write(repr(msg.latitude) + "," + repr(msg.longitude)+"\n")
        except pynmea2.ParseError as e:
            print('Parse error: {}'.format(e))
            continue
file_final.close()