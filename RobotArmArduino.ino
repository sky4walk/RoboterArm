#include <SoftwareSerial.h>
#include <Servo.h>
 
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
  if( 2 <= bluetooth.available() )
  {
    unsigned int servoNr = bluetooth.read();
    unsigned int servoPos = bluetooth.read();
    Serial.println(servoNr);
    Serial.println(servoPos);
 
    if ( 1 == servoNr ) {
      myservo1.write(servoPos);
    }
    else if ( 2 == servoNr ) {
      myservo2.write(servoPos);
    }
    else if ( 3 == servoNr ) {
      myservo3.write(servoPos);
    }
    else if ( 4 == servoNr ) {
      myservo4.write(servoPos);
    }
    delay(15);
  }
  if( 2 <= Serial.available() )
  {
    unsigned int servoNr = Serial.read();
    unsigned int servoPos = Serial.read();
    Serial.println(servoNr);
    Serial.println(servoPos);
 
    if ( 1 == servoNr ) {
      myservo1.write(servoPos);
    }
    else if ( 2 == servoNr ) {
      myservo2.write(servoPos);
    }
    else if ( 3 == servoNr ) {
      myservo3.write(servoPos);
    }
    else if ( 4 == servoNr ) {
      myservo4.write(servoPos);
    }
    delay(15);
  }
}