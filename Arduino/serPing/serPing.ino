void setup() {
  if (Serial) {
    Serial.end();
  }
  Serial.begin(9600);
  while (!Serial) {    
  }
  Serial.println("ready");
}

void loop() {
  if( 0 < Serial.available() ) {
    int rec = Serial.read();
    Serial.write((char)rec);
  }
}
