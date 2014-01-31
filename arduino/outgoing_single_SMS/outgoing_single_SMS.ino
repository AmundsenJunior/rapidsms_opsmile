#include <SoftwareSerial.h>
SoftwareSerial SIM900(7, 8);

void setup()
{
  SIM900.begin(19200);
  SIM900power();
  delay(20000);
}

void SIM900power()
{
  digitalWrite(9, HIGH);
  delay(1000);
  digitalWrite(9, LOW);
  delay(5000);
}

void sendSMS()
{
  SIM900.print("AT+CMGF=1\r");
  delay(100);
  SIM900.println("AT + CMGS = \"+1##########\"");
  delay(100);
  SIM900.println("Hi, this is Operation Smile, texting you from the Arduino.");
  delay(100);
  SIM900.println((char)26);
  delay(100);
  SIM900.println();
  delay(5000);
  SIM900power();
}

void loop()
{
  sendSMS();
  do {} while (1);
}

