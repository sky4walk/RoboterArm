import time
import maestro
servo = maestro.Controller("COM13")

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
servo.setTarget(1,6940)
servo.setTarget(2,5180)
servo.setTarget(0,6000)
servo.setTarget(3,5864)
#close door
servo.setTarget(4,3968)
time.sleep(3)
i = 0

while i < 100:
#start 
    servo.setTarget(0,6252)  
    servo.setTarget(1,5380)  
    servo.setTarget(2,6101)  
    servo.setTarget(2,7177)  
    time.sleep(3)
    servo.setTarget(4,7000) 
    time.sleep(1)
    servo.setTarget(3,4788)  
    time.sleep(3)
    servo.setTarget(1,5432)
    time.sleep(1)
    servo.setTarget(2,6101)
    time.sleep(1)
    servo.setTarget(0,6227)
    time.sleep(1)
    servo.setTarget(1,8000)
    time.sleep(1)
    servo.setTarget(0,4813)
    time.sleep(2)
    servo.setTarget(2,6786)
    time.sleep(2)
    servo.setTarget(4,3948)
    time.sleep(1)
    servo.setTarget(3,5864)
    time.sleep(2)
    servo.setTarget(2,5180)
    time.sleep(1)	
    servo.setTarget(1,6940)    
    servo.setTarget(0,6000)
    servo.setTarget(3,5864)
    time.sleep(1)
    i += 1
	
servo.close()