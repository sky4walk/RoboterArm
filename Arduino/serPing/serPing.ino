void setup() {
  Serial.begin(9600);
}

void loop() {
  if( 1 <= Serial.available() ) {
    int rec = Serial.read();
    Serial.write((char)rec);
  }
}
