# install serial from 
# https://pypi.org/project/pyserial/
# https://pythonhosted.org/pyserial/
# https://github.com/pyserial/pyserial
# pip --proxy=http://proxy:81 install pyserial
import time
import serial

port = "COM10"
baud = 9600

startPosXAxle  = 0
startPosYLift  = 0
startPosYArm   = 0
startPosHand   = 0
startPosMarble = 0

moveSteps = 2

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
    print("Move by Hand")
    print("a Z-Axle left")
    print("d Z-Axle right")
    print("w Y-Lift Arm up")
    print("s Y-Lift Arm down")
    print("x Hand open")
    print("y Hand close")
    print("e exit")
    key = getch(1).decode('utf-8')
    sendRecv(ser,b'1234')
    nextState = 2
    if   key == 'a' :
        nextState = 2
    elif key == 'd' :
        nextState = 2
    elif key == 'w' :
        nextState = 2
    elif key == 's' :
        nextState = 2
    elif key == 'x' :
        nextState = 2
    elif key == 'y' :
        nextState = 2
    elif key == 'e' :
        nextState = 1
    else :
        nextState = 1
    return nextState
    
def getStartPos(ser):
    #magic command
    ser.write(b'1999')
    respondStr = ser.readline().decode('utf-8')
    print("Z-Axle",respondStr)
    respondStr = ser.readline().decode('utf-8')
    print("Y-Lift",respondStr)
    respondStr = ser.readline().decode('utf-8')
    print("Y-Lift Arm up",respondStr)
    respondStr = ser.readline().decode('utf-8')
    print("Hand",respondStr)
    respondStr = ser.readline().decode('utf-8')
    print("Marble",respondStr)
    
def mainLoop():
    ser = startSerial()
    waitForArduino(ser)
    getStartPos(ser)

    state = 1
    while 0 < state :
        if   1 == state :
            state = mainMenu()
        elif 2 == state :
            state = moveByHand(ser)
        else :
            state = 0
        
mainLoop()
