#include <SoftwareSerial.h>
#include <Servo.h>
#define ASCII_DIFF 48
#define MOVE_DELAY 100
int bluetoothTx = 6;
int bluetoothRx = 7;
 
Servo myservo1, myservo2, myservo3, myservo4;
SoftwareSerial bluetooth(bluetoothTx, bluetoothRx);
 
void setup()
{
  myservo1.attach(8);
  myservo2.attach(9);
  myservo3.attach(10);
  myservo4.attach(11);
 
  Serial.begin(9600);
  bluetooth.begin(9600);
}
 
void loop()
{
if( 4 <= bluetooth.available() )
  {
    unsigned int servoNr     = bluetooth.read() - ASCII_DIFF;
    unsigned int servoPosIn1 = bluetooth.read() - ASCII_DIFF;
    unsigned int servoPosIn2 = bluetooth.read() - ASCII_DIFF;
    unsigned int servoPosIn3 = bluetooth.read() - ASCII_DIFF;
    bluetooth.read();
    bluetooth.read();
    unsigned int servoPos = servoPosIn1*100+servoPosIn2*10+servoPosIn3;
    Serial.print("Servo:");
    Serial.print(servoNr);
    Serial.print(" Pos:");
    Serial.print(servoPos);
 
    if ( 1 == servoNr ) {
      myservo1.write(servoPos);
      Serial.println(" On 1");
    }
    else if ( 2 == servoNr ) {
      myservo2.write(servoPos);
      Serial.println(" On 2");
    }
    else if ( 3 == servoNr ) {
      myservo3.write(servoPos);
      Serial.println(" On 3");
    }
    else if ( 4 == servoNr ) {
      myservo4.write(servoPos);
      Serial.println(" On 4");
    }
    else {
      Serial.println(" Off");
    }
    delay(MOVE_DELAY);
  }
  if( 4 <= Serial.available() )
  {
    unsigned int servoNr     = Serial.read() - ASCII_DIFF;
    unsigned int servoPosIn1 = Serial.read() - ASCII_DIFF;
    unsigned int servoPosIn2 = Serial.read() - ASCII_DIFF;
    unsigned int servoPosIn3 = Serial.read() - ASCII_DIFF;
    Serial.read();
    Serial.read();
    unsigned int servoPos = servoPosIn1*100+servoPosIn2*10+servoPosIn3;
    Serial.print("Servo:");
    Serial.print(servoNr);
    Serial.print(" Pos:");
    Serial.print(servoPos);
 
    if ( 1 == servoNr ) {
      myservo1.write(servoPos);
      Serial.println(" On 1");
    }
    else if ( 2 == servoNr ) {
      myservo2.write(servoPos);
      Serial.println(" On 2");
    }
    else if ( 3 == servoNr ) {
      myservo3.write(servoPos);
      Serial.println(" On 3");
    }
    else if ( 4 == servoNr ) {
      myservo4.write(servoPos);
      Serial.println(" On 4");
    }
    else {
      Serial.println(" Off");
    }
    delay(MOVE_DELAY);
  }
}
