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

servo.setAccel(4,0)      #set servo 0 acceleration to 4
servo.setSpeed(4,0)     #set speed of servo 1

#save arm
servo.setTarget(3,5420)
time.sleep(2)
servo.setTarget(0,5268)
servo.setTarget(1,7920)
servo.setTarget(2,5380)
time.sleep(2)

#take pencil
servo.setTarget(0,5268)  
servo.setTarget(1,6492)  
servo.setTarget(2,8000)  
time.sleep(2)
servo.setTarget(3,4516)  


servo.close()