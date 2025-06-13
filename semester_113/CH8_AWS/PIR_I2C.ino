#include <Wire.h>
byte TxByte =0x00;
int sensor = 9;

void I2C_TxHandler(void){
  Wire.write(TxByte);
}

void setup() {
  // put your setup code here, to run once:
  Wire.begin(0x55);
  Wire.onRequest(I2C_TxHandler);
  Serial.begin(9600);
  pinMode(sensor, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int moving = digitalRead(sensor);
  if(moving==1){
    Serial.println("moving");
    TxByte = 0xAA;
  }
  else{
    Serial.println("Stop");
    TxByte = 0x00;
  }
  delay(50);
}
