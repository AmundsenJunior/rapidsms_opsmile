# Python interface for communication with Arduino-GSM Shield

#import pySerial library
import serial

# Boolean for whether Arduino is connected
connect = False

# Open serial port interface
ser = serial.Serial('/dev/ttyACM0',19200)

# loop until Arduino sends a ready message
while not connected:
	serin = ser.read()
	connected = True

# Read new data incoming from Arduino,
# where "i" is a case initializer in the Arduino code.
ser.write("i")

# Pass commands and data to the Arduino
ser.write("o"+str(outgoingMessage))


# Close interface
ser.close()

