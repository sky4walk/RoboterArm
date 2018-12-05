#include <SoftwareSerial.h>
#include <Servo.h>

#define ASCII_DIFF 48
#define MOVE_DELAY 500

int bluetoothTx = 6;
int bluetoothRx = 7;

int startPosZAxle  = 90;
int startPosYLift  = 100;
int startPosYArm   = 40;
int startPosHand   = 65;
int startPosMarble = 60;
unsigned int showPosCmd = 999;

Servo myservo1, myservo2, myservo3, myservo4, myservo5;
SoftwareSerial bluetooth(bluetoothTx, bluetoothRx);

void setup()
{
  if (Serial) {
    Serial.end();
  }
  Serial.begin(9600);
  while (!Serial) {
    ;
  }

  myservo1.attach(8);
  myservo2.attach(9);
  myservo3.attach(10);
  myservo4.attach(11);
  myservo5.attach(12);

  bluetooth.begin(9600);

  Serial.println("ready");
  bluetooth.println("ready");

  myservo1.write(startPosZAxle);
  delay(MOVE_DELAY);
  myservo2.write(startPosYLift);
  delay(MOVE_DELAY);
  myservo3.write(startPosYArm);
  delay(MOVE_DELAY);
  myservo4.write(startPosHand);
  delay(MOVE_DELAY);
  myservo5.write(startPosMarble);
  delay(MOVE_DELAY);
}

void printPositions() {
  int read1 = myservo1.read();
  Serial.println(read1);
  bluetooth.println(read1);

  int read2 = myservo2.read();
  Serial.println(read2);
  bluetooth.println(read2);

  int read3 = myservo3.read();
  Serial.println(read3);
  bluetooth.println(read3);

  int read4 = myservo4.read();
  Serial.println(read4);
  bluetooth.println(read4);

  int read5 = myservo5.read();
  Serial.println(read5);
  bluetooth.println(read5);
}

void loop()
{
  boolean received = false;
  unsigned int servoNr = 0;
  unsigned int servoPosIn1 = 0;
  unsigned int servoPosIn2 = 0;
  unsigned int servoPosIn3 = 0;

  if ( 4 <= bluetooth.available() ) {
    servoNr     = bluetooth.read() - ASCII_DIFF;
    servoPosIn1 = bluetooth.read() - ASCII_DIFF;
    servoPosIn2 = bluetooth.read() - ASCII_DIFF;
    servoPosIn3 = bluetooth.read() - ASCII_DIFF;
    received = true;
  }
  else if ( 4 <= Serial.available() ) {
    servoNr     = Serial.read() - ASCII_DIFF;
    servoPosIn1 = Serial.read() - ASCII_DIFF;
    servoPosIn2 = Serial.read() - ASCII_DIFF;
    servoPosIn3 = Serial.read() - ASCII_DIFF;
    received = true;
  }
  if ( true == received ) {
    unsigned int servoPos = servoPosIn1 * 100 + servoPosIn2 * 10 + servoPosIn3;
    while ( bluetooth.available() ) {
      bluetooth.read();
    }
    while ( Serial.available() ) {
      Serial.read();
    }

    if ( showPosCmd == servoPos ) {
      printPositions();
    } else {

      bluetooth.print("Servo:");
      bluetooth.print(servoNr);
      bluetooth.print(" Pos:");
      bluetooth.print(servoPos);

      Serial.print("Servo:");
      Serial.print(servoNr);
      Serial.print(" Pos:");
      Serial.print(servoPos);

      if ( 1 == servoNr ) {
        myservo1.write(servoPos);
        bluetooth.println(" On 1");
        Serial.println(" On 1");
      }
      else if ( 2 == servoNr ) {
        myservo2.write(servoPos);
        bluetooth.println(" On 2");
        Serial.println(" On 2");
      }
      else if ( 3 == servoNr ) {
        myservo3.write(servoPos);
        bluetooth.println(" On 3");
        Serial.println(" On 3");
      }
      else if ( 4 == servoNr ) {
        myservo4.write(servoPos);
        bluetooth.println(" On 4");
        Serial.println(" On 4");
      }
      else if ( 5 == servoNr ) {
        myservo5.write(servoPos);
        bluetooth.println(" On 5");
        Serial.println(" On 5");
      }
      else {
        bluetooth.println(" Off");
        Serial.println(" Off");
      }
    }
  }
  delay(MOVE_DELAY);
}
