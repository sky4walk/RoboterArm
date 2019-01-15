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
servo.setTarget(3,5560)
time.sleep(2)

servo.setTarget(1,7920)
servo.setTarget(2,5380)
time.sleep(2)
servo.setTarget(0,5268)

#take pencil
servo.setTarget(0,5300)  
time.sleep(3)
servo.setTarget(1,6940)  
servo.setTarget(2,7608)  
time.sleep(2)
servo.setTarget(3,4180)  
time.sleep(3)
servo.setTarget(1,7804)  
servo.setTarget(2,7020)  
time.sleep(1)
servo.setTarget(1,7920)
servo.setTarget(2,5380)
time.sleep(1)
servo.setTarget(0,8280)
time.sleep(1)
#position knopf 1
servo.setTarget(1,6312)
servo.setTarget(2,6796)
time.sleep(5)
#druecke Knopf 1
servo.setAccel(0,4)     
servo.setSpeed(0,20)     
servo.setAccel(1,4)     
servo.setSpeed(1,20)     
servo.setTarget(1,5964)
time.sleep(2)
servo.setTarget(1,6312)
#fahre zu knopf 2
time.sleep(1)
servo.setTarget(0,9116)
servo.setTarget(1,6312)
servo.setTarget(2,5828)
time.sleep(1)
#schleife druecken
i = 0
while i < 5:
  servo.setTarget(1,5760)
  time.sleep(1)
  servo.setTarget(1,5536)
  time.sleep(1)
  i += 1

servo.setTarget(1,6000)

servo.setTarget(1,7920)
servo.setTarget(2,5380)
time.sleep(2)
servo.setTarget(0,5268)

#take back pencil
servo.setTarget(1,7920)
servo.setTarget(2,5380)
time.sleep(2)
servo.setTarget(0,5300)  
time.sleep(1)
servo.setTarget(1,7240)
servo.setTarget(2,7340)  
time.sleep(2)
servo.setTarget(3,5560) 

servo.close()