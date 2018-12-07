# install serial from 
# https://pypi.org/project/pyserial/
# https://pythonhosted.org/pyserial/
# https://github.com/pyserial/pyserial
# pip --proxy=http://proxy:81 install pyserial
import time
import serial

port = "COM10"
baud = 9600

startPosZAxle  = 0
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
    try:
        serCon = serial.Serial(port, baud, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE )
    except serial.SerialException as e:
        print("connection to ",port,"not possible")
        quit()
    return serCon

def getch(length=1):
    if msvcrt:
        char = msvcrt.getch()
        if char in ('\000', '\xe0'):
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
    startStr = ser.readline().decode('utf-8').rstrip('\r\n')
    if startStr != "ready":
        print("no connection")
        quit()	

def mainMenu():
    print("Menu")
    print("----")    
    print("h  Movement by hand")
    print("m  Marble Run")
    print("t  Test Display Buttons")
    print("r  Read positions")
    print("e  exit")
    key = getch(1).decode('utf-8')
    if   key == 'h' :
        nextState = 2
    elif key == 'm' :
        nextState = 3
    elif key == 't' :
        nextState = 4
    elif key == 'r' :
        printStartPos()
        nextState = 1
    elif key == 'e' :
        nextState = 0
    else :
        nextState = 1    
    return int(nextState)

def printStartPos():
    print("Z-Axle\t",startPosZAxle)
    print("Y-Lift\t",startPosYLift)
    print("Y-Arm\t",startPosYArm)
    print("Hand\t",startPosHand)
    print("Marble\t",startPosMarble)
    
def moveByHand(ser):
    global startPosZAxle
    global startPosYLift
    global startPosYArm
    global startPosHand
    global startPosMarble

    print("Move by Hand")
    print("------------")
    print("4 Z-Axle left")
    print("6 Z-Axle right")
    print("7 Y-Lift up")
    print("1 Y-Lift down")
    print("8 Y-Lift up")
    print("2 Y-Lift down")
    print("9 Hand open")
    print("3 Hand close")
    print("+ Marble open")
    print("- Marble close")
    print("e back")
    key = getch(1).decode('utf-8')
    nextState = 2
    if   key == '4' :
        startPosZAxle = startPosZAxle + moveSteps
        sendStr = "1" + str(startPosZAxle).zfill(3) 
        sendRecv(ser,sendStr.encode('utf-8'))
        nextState = 2
    elif key == '6' :
        startPosZAxle = startPosZAxle - moveSteps
        sendStr = "1" + str(startPosZAxle).zfill(3) 
        sendRecv(ser,sendStr.encode('utf-8'))
        nextState = 2
    elif key == '7' :
        startPosYLift = startPosYLift + moveSteps
        sendStr = "2" + str(startPosYLift).zfill(3) 
        sendRecv(ser,sendStr.encode('utf-8'))
        nextState = 2
    elif key == '1' :
        startPosYLift = startPosYLift - moveSteps
        sendStr = "2" + str(startPosYLift).zfill(3) 
        sendRecv(ser,sendStr.encode('utf-8'))
        nextState = 2
    elif key == '8' :
        startPosYArm = startPosYArm + moveSteps
        sendStr = "3" + str(startPosYArm).zfill(3) 
        sendRecv(ser,sendStr.encode('utf-8'))
        nextState = 2
    elif key == '2' :
        startPosYArm = startPosYArm - moveSteps
        sendStr = "3" + str(startPosYArm).zfill(3) 
        sendRecv(ser,sendStr.encode('utf-8'))
        nextState = 2
    elif key == '9' :
        startPosHand = startPosHand + moveSteps
        sendStr = "4" + str(startPosHand).zfill(3) 
        sendRecv(ser,sendStr.encode('utf-8'))
        nextState = 2
    elif key == '3' :
        startPosHand = startPosHand - moveSteps
        sendStr = "4" + str(startPosHand).zfill(3) 
        sendRecv(ser,sendStr.encode('utf-8'))
        nextState = 2
    elif key == '+' :
        startPosMarble = startPosMarble + moveSteps
        sendStr = "5" + str(startPosMarble).zfill(3) 
        sendRecv(ser,sendStr.encode('utf-8'))
        nextState = 2
    elif key == '-' :
        startPosMarble = startPosMarble - moveSteps
        sendStr = "5" + str(startPosMarble).zfill(3) 
        sendRecv(ser,sendStr.encode('utf-8'))
        nextState = 2
    elif key == 'e' :
        nextState = 1
    else :
        nextState = 1
    return nextState
    
def getStartPos(ser):
    global startPosZAxle
    global startPosYLift
    global startPosYArm
    global startPosHand
    global startPosMarble
    #magic command
    ser.write(b'1999')
    respondStr = ser.readline().decode('utf-8').rstrip('\r\n')
    startPosZAxle = int(respondStr)
    respondStr = ser.readline().decode('utf-8').rstrip('\r\n')
    startPosYLift = int(respondStr)
    respondStr = ser.readline().decode('utf-8').rstrip('\r\n')
    startPosYArm = int(respondStr)
    respondStr = ser.readline().decode('utf-8').rstrip('\r\n')
    startPosHand = int(respondStr)
    respondStr = ser.readline().decode('utf-8').rstrip('\r\n')
    startPosMarble = int(respondStr)

def marbleRun(ser):
    nextState = 1
    return nextState

def testDisplayButtons(ser):
    nextState = 1
    return nextState
    
    
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
        elif 3 == state :
            state = marbleRun(ser)
        elif 4 == state :
            state = testDisplayButtons(ser)
        else :
            state = 0
        
mainLoop()
