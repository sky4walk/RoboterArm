# install serial from 
# https://pypi.org/project/pyserial/
# https://pythonhosted.org/pyserial/
# https://github.com/pyserial/pyserial
# pip --proxy=http://proxy:81 install pyserial
import time
import serial

try:
    # windows
    import msvcrt
except ImportError:
    msvcrt = None
    import sys
    import termios
    import tty

def getch(length=1):
    """
    Read a key press and return the result. Nothing is echoed to the
    console.

    Note that on Windows a special function key press will return its
    keycode. `Control-C` cannot be read there.

    On Unices it will return one char by default. Thus, when reading
    a special function key, whose resulting escape sequence could be
    longer than one char, the `length` value might be changed, since
    otherwise the remaining characters would be returned by the next
    calls until stdin is "empty".
    """
    if msvcrt:
        char = msvcrt.getch()
        if char in ('\000', '\xe0'):
            # special key -> need a second call to get keycode
            char = msvcrt.getch()
        return char
    else:
        old = termios.tcgetattr(sys.stdin)
        try:
            tty.setraw(sys.stdin)
            return sys.stdin.read(length)
        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old)
			
port = "COM10"
baud = 9600

ser = serial.Serial(port, baud, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE )
time.sleep(2)
startStr = ser.readline().decode('utf-8')

if startStr != "ready\r\n":
    print("no connection")
    quit()

print("Menu")
print("1  Movement by hand")
print("2  Marble Run")
print("3  Test Display Buttons")

key = getch(1)
print(key)
	
ser.write(b'1234')
respondStr = ser.readline().decode('utf-8')
print(respondStr)
