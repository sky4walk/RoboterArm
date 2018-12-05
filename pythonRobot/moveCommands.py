# install serial from 
# https://pypi.org/project/pyserial/
# https://pythonhosted.org/pyserial/
# https://github.com/pyserial/pyserial
# pip --proxy=http://proxy:81 install pyserial
import time
import serial

port = "COM10"
baud = 9600

try:
    # windows
    import msvcrt
except ImportError:
    msvcrt = None
    import sys
    import termios
    import tty

def startSerial():
    serCon = serial.Serial(port, baud, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE )
    return serCon

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

def sendRecv(ser,bytesSend):
    ser.write(bytesSend)
    respondStr = ser.readline().decode('utf-8')
    strList = respondStr.split(" ")
    if 4 != len(strList) :
        print ("Recv error")
    else :
        strMotor = strList[0].split(":")
        strMove = strList[1].split(":")
        strWork = strList[3].split("\r\n")
        if 2 != len(strMotor) or 2 != len(strMove) or 2 != len(strWork) :
            print ("Recv error")
        else :
            if "Servo" == strMotor[0] :
                if   1 == int(strMotor[1]) :
                    print("Z-Axle")
                elif 2 == int(strMotor[1]) :
                    print("Y-Lift Arm")
                elif 3 == int(strMotor[1]) :
                    print("X-Move Arm")
                elif 4 == int(strMotor[1]) :
                    print("Hand")
                elif 5 == int(strMotor[1]) :
                    print("Marble door")
                else :
                    print("unknown servo")
            if "Pos" == strMove[0] :
                print("Position",strMove[1])
            if strWork[0] == strMotor[1] :
                print("OK")
            else :
                print("wrong")
	
def waitForArduino(ser):
    time.sleep(2)
    startStr = ser.readline().decode('utf-8')
    if startStr != "ready\r\n":
        print("no connection")
        quit()	

def mainMenu():
    print("Menu")
    print("h  Movement by hand")
    print("m  Marble Run")
    print("t  Test Display Buttons")
    print("e  exit")
    key = getch(1).decode('utf-8')
    if   key == 'h' :
        nextState = 2
    elif key == 'm' :
        nextState = 3
    elif key == 't' :
        nextState = 4
    elif key == 'e' :
        nextState = 0
    else :
        nextState = 1    
    return int(nextState)

def moveByHand(ser):
    sendRecv(ser,b'1234')
    return 1

def mainLoop():
    ser = startSerial()
    waitForArduino(ser)

    state = 1
    while 0 < state :
        if   1 == state :
            state = mainMenu()
        elif 2 == state :
            state = moveByHand(ser)
        else :
            state = 0
        
mainLoop()
