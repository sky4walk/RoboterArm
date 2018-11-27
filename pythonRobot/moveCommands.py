# install serial from 
# https://pypi.org/project/pyserial/
# https://github.com/pyserial/pyserial
# pip --proxy=http://proxy:81 install pyserial
import serial
import serial.tools.list_ports as port_list

ports = list(port_list.comports())
for p in ports:
    print (p)
	
ser = serial.Serial("COM9", 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE )
ser.write(b'1')
x = ser.readline()
print(x)