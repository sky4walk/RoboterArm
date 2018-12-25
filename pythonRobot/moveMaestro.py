import time
import maestro
servo = maestro.Controller("COM5")

servo.setAccel(0,4)      #set servo 0 acceleration to 4
servo.setSpeed(0,10)     #set speed of servo 1

servo.setAccel(1,4)      #set servo 0 acceleration to 4
servo.setSpeed(1,10)     #set speed of servo 1

servo.setAccel(2,4)      #set servo 0 acceleration to 4
servo.setSpeed(2,10)     #set speed of servo 1

servo.setAccel(3,4)      #set servo 0 acceleration to 4
servo.setSpeed(3,10)     #set speed of servo 1

servo.setAccel(4,4)      #set servo 0 acceleration to 4
servo.setSpeed(4,10)     #set speed of servo 1

servo.setTarget(0,6000)  #set servo to move to center position
time.sleep(2)
servo.setTarget(0,6373)  #set servo to move to center position

time.sleep(2)
servo.setTarget(1,4516)  #set servo to move to center position


servo.close()