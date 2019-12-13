#include<Wire.h>
#include<SoftwareSerial.h>
const int MPU6050_addr=0x68;
float AccX,AccY,AccZ;
int pwmPin = A2; // assigns pin 12 to variable pwm
int pot = A0; // assigns analog input A0 to variable pot
int c1 = 0;   // declares variable c1
int c2 = 0;   // declares variable c2
int tx=7;
int rx=6;
SoftwareSerial bt(tx,rx);
void setup(){
  pinMode(pwmPin, OUTPUT); 
  pinMode(pot, INPUT); 
  pinMode(tx, OUTPUT); 
  pinMode(rx, INPUT);
  Wire.begin();
  Wire.beginTransmission(MPU6050_addr);
  Wire.write(0x6B);
  Wire.write(0);
  Wire.endTransmission(true);
  Serial.begin(9600);
}
void loop(){
  Wire.beginTransmission(MPU6050_addr);
  Wire.write(0x3B);
  Wire.endTransmission(false);
  Wire.requestFrom(MPU6050_addr,6,true);
  AccX=Wire.read()<<8|Wire.read();
  AccY=Wire.read()<<8|Wire.read();
  AccZ=Wire.read()<<8|Wire.read();
  AccX = AccX/16384;
  AccY = AccY/16384;
  AccZ = AccZ/16384;
  if (AccZ>0.93){
    Serial.println("Top Molars");
  }
  else if (AccX <-0.90){
    Serial.println("Incisors");
      
  }
  
  
  else if (AccZ<-0.93){
    Serial.println("Bottom Molars");
  }

  if(Serial.available())
  {
    char x;
    bt.begin(9600);
    x=Serial.read();
    bt.write(x);
    
  }
  c2= analogRead(pot); 
  c1= 1024-c2;       
  Serial.println(c1);
  analogWrite(pwmPin, c2);  
  delay(100);
}
