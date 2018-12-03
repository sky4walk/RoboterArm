# install serial from 
# https://pypi.org/project/pyserial/
# https://pythonhosted.org/pyserial/
# https://github.com/pyserial/pyserial
# pip --proxy=http://proxy:81 install pyserial
import threading
import time
import serial
import serial.tools.list_ports as port_list

ports = list(port_list.comports())
for p in ports:
    print (p)

