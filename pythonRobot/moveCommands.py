# install serial from 
# https://pypi.org/project/pyserial/
# https://pythonhosted.org/pyserial/
# https://github.com/pyserial/pyserial
# pip --proxy=http://proxy:81 install pyserial
import threading
import time
import serial
import serial.tools.list_ports as port_list

port = "COM10"
baud = 9600

ser = serial.Serial(port, baud, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE )
time.sleep(2)
startStr = ser.readline().decode('utf-8')

if startStr != "ready\r\n":
  print("no connection")
  quit()

ser.write(b'1234')
respondStr = ser.readline().decode('utf-8')
print(respondStr)
