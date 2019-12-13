#include<Wire.h>
#include<SoftwareSerial.h>

// Define the data transmit/receive pins in Arduino

const int MPU6050_addr=0x68;
float AccX,AccY,AccZ;
int pwmPin1 = A2; // assigns pin 12 to variable pwm
int pwmPin2 = A3; //

int pot1 = A0; // assigns analog input A0 to variable pot1
int pot2 = A1; // assigns analog input A1 to variable pot2

int c1 = 0;   // declares variable c1
int c2 = 0;   // declares variable c2

int TxD = 0;
int RxD = 1;

//int StartTime = millis();  

SoftwareSerial bt(RxD,TxD);

void setup(){
  pinMode(pot1,INPUT);
  pinMode(pot2,INPUT);
  
  pinMode(pwmPin1, OUTPUT);
  pinMode(pwmPin2,OUTPUT);
 
  pinMode(TxD, OUTPUT);
  pinMode(RxD, INPUT);
  Wire.begin();
  Wire.beginTransmission(MPU6050_addr);
  Wire.write(0x6B);
  Wire.write(0);
  Wire.endTransmission(true);
  Serial.begin(9600);
  bt.begin(9600);
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
  Serial.print(AccX); 
  Serial.print(AccY);
  Serial.println(AccZ);
  if (AccZ>0.90){
   Serial.println("Incisors ");
  }
  else if (AccX >0.90){
    Serial.println("Top Molars ");
  }
  else if (AccX<0.90){
    Serial.println("Bottom Molars ");
      }

         
  c1 = analogRead(pot1);      
  c2 = analogRead(pot2);

  analogWrite(pwmPin1, c1);
  analogWrite(pwmPin2, c2);
 Serial.println(c1);
  delay(400);
}
