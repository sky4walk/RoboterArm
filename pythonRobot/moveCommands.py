# install serial from 
# https://pypi.org/project/pyserial/
# https://github.com/pyserial/pyserial
# pip --proxy=http://proxy:81 install pyserial
import threading
import time
import serial
import serial.tools.list_ports as port_list

port = "COM9"
baud = 9600

ports = list(port_list.comports())
for p in ports:
    print (p)

	
#ser = serial.Serial(port, baud, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE )

#while (True):
#    ser.write(b'1')
#    print("sende")
#    if (ser.inWaiting() > 0):
#        data_str = ser.read(ser.inWaiting()).decode('ascii')
#        print(data_str, end='')
#    time.sleep(0.01)	

serial_port = serial.Serial(port, baud, timeout=0)

def read_from_port(ser):
    while True:
        print("test")
        ser.write(b'1')
        reading = ser.read()
        print(reading)

thread = threading.Thread(target=read_from_port, args=(serial_port,))
thread.start()		
