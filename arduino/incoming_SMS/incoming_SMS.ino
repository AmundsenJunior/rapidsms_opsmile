#include <SoftwareSerial.h>
SoftwareSerial SIM900(7, 8);

char incoming_char=0;

void setup()
{
  Serial.begin(19200);
  SIM900.begin(19200);
  SIM900power();
  delay(20000);
  
  SIM900.print("AT+CMGF=1\r"); // set SMS mode to text
  delay(100);
  SIM900.print("AT+CNMI=2,2,0,0,0\r");
  delay(100);
}

void SIM900power()
{
  digitalWrite(9, HIGH);
  delay(1000);
  digitalWrite(9, LOW);
  delay(7000);
}

void loop()
{
  if(SIM900.available() >0)
  {
    incoming_char=SIM900.read();
    Serial.print(incoming_char);
  }
}

