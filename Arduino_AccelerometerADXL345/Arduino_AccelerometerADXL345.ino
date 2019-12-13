#include<Wire.h>
const int MPU6050_addr=0x68;
float AccX,AccY,AccZ,Temp,GyroX,GyroY,GyroZ;
void setup(){
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
  Temp=Wire.read()<<8|Wire.read();
  GyroX=Wire.read()<<8|Wire.read();
  GyroY=Wire.read()<< 8|Wire.read();
  GyroZ=Wire.read()<<8 |Wire.read();
  AccX = AccX/16384;
  AccY = AccY/16384;
  AccZ = AccZ/16384;
  Serial.print("AccX = "); Serial.print(AccX);
  Serial.print(" || AccY = "); Serial.print(AccY);
  Serial.print(" || AccZ = "); Serial.println(AccZ);
  //Serial.print(" || Temp = "); Serial.print(Temp/340.00+36.53);
  //Serial.print(" || GyroX = "); Serial.print(GyroX);
  //Serial.print(" || GyroY = "); Serial.print(GyroY);
  //Serial.print(" || GyroZ = "); Serial.println(GyroZ);
  delay(10);
}
