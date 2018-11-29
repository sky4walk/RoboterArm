# install serial from 
# https://pypi.org/project/pyserial/
# https://pythonhosted.org/pyserial/
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

ser = serial.Serial(port, baud, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE )
time.sleep(2)
startStr = ser.readline()
print(startStr)