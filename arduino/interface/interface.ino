#include <SoftwareSerial.h>
SoftwareSerial SIM900(7, 8);

char incoming_char=0;

void setup()
{
  Serial.begin(19200);
  SIM900.begin(19200);
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
  while(Serial.available() == 0)
  {
    if(SIM900.available() >0)
    {
      incoming_char=SIM900.read();
      Serial.print(incoming_char);
    }
    char inByte = Serial.read();
    switch(inByte)
    {
      case 'o':
        String phNum = phoneNumber();
        Serial.print(phNum);
        SIM900.println("AT+CMGS=\"+"+phNum+"\"");
        delay(100);
        String repMsg = replyMessage();
        Serial.print(repMsg);
        SIM900.println("\""+repMsg+"\"");
        delay(100);
        SIM900.println((char)26);
        delay(100);
        SIM900.println();
        delay(100);
        SIM900.print("AT+CMNI=2,2,0,0,0\r");
        delay(100);
        break;
      }
    Serial.flush();
  }
}

String phoneNumber(void)
{
  String numberString = "";
  unsigned char index=0;
  delay(10);
  while(Serial.available() > 0)
  {
    delay(10);
    numberString+=Serial.read();
    index++;
    if(index>10)
    {
      break;
    }
  }
  return numberString;
}

String replyMessage(void)
{
  String textString = "";
  unsigned char index=0;
  delay(10);
  while(Serial.available() > 0)
  {
    delay(10);
    textString += Serial.read();
    index++;
    if(index>139)
    {
      break;
    }
  }
  return textString;
}

