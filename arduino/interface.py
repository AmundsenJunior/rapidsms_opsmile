# Python interface for communication with Arduino-GSM Shield

#import pySerial library
import serial
from app import handle

# Boolean for whether Arduino is connected
connected = False

# Open serial port interface
ser = serial.Serial('/dev/ttyACM0',19200)

# loop until Arduino sends a ready message
while not connected:
	serin = ser.read()
	connected = True

while connected:

	# Read lines printed by Arduino
	line = ser.readline()
	print line

	# Ignore account balance messages
	#if line[:16] == '+CMT: "78108858"':
	#	ser.readline()
		
	if line[:4] == '+CMT':
		#print line
		ph_num = line[8:19]
		print ph_num
		text = ser.readline()
		print text
		out_msg = handle(text)
		print out_msg
		ser.write('o')
		ser.write(str(ph_num))
		ser.write(str(out_msg))


# Request new data incoming from Arduino,
# where "i" is a case initializer in the Arduino code.
# ser.write("i")


# Pass commands and data to the Arduino
#ser.write("o"+str(ph_num)+"\r"+str(outgoingMessage))


# Close interface
ser.close()

