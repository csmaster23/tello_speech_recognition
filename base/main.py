# Tanner Norton - Tello Project - Started October 2019
# MUST BE RUN IN PYTHON3 **

# imports
import sys
import time
import pyttsx3
from easytello import tello

import Speech_Recognition 	as sr
import Computer_Speech		as cs
import Process_Commands		as pc

import time
from threading import Thread

def timer(drone):
	print("\n---Top of timer method---\n")
	count = 0
	up_down = True
	while count < 201:
		drone.cw(90)
		time.sleep(10)
		count += 10
		print("\nHi, this program has now been running for " + str(count) + " seconds.\n")
		# if up_down:
		# 	drone.up(10)
		# 	up_down = False
		# else:
		# 	drone.down(10)
		# 	up_down = True
	print("\n---We waited for a total of %s seconds\n" % str(count))
	sys.exit(0)

def main():
	sys.stdout.write("---------Top of the main method in main.py-----------\n")
	engine = pyttsx3.init()
	sys.stdout.write("---------Attempting to connect with tello------------\n")
	connect_bool = False

	while not connect_bool:
		print("---Top of While---")
		drone = tello.Tello()
		if drone != None:
			connect_bool = True

	drone.takeoff()

	print("---After takeoff---\n")

	background_thread = Thread(target=timer, args=(drone,))
	background_thread.start()

	# initialisation for computer's ability to speak
	operating = True
	while operating:
		#print("\n---Top of operating while loop---")
		speech_command, number, type = sr.Recognize()
		print("---Resulting speech command in main.py: %s and the associated number: %s and the type: %s----" % (speech_command, str(number), type))

		if 'end program' in speech_command.lower():
			operating = False
			continue

		#drone = None
		#cs.Speak("Command attempting to execute", engine)
		#cs.Speak(speech_command, engine)
		pc.Process(speech_command, drone, type, number)
		#print("\n---------After pc.Process has executed the command---------\n")

		#print("---Sleep 10 seconds---")
		#time.sleep(10)
		#drone = tello.Tello()
		#drone.takeoff()
		#time.sleep(3)
		# -----PROCESSING OF CONFIRMED COMMAND TAKES PLACE----------



		#cs.Speak("Command has been executed.", engine)
		#cs.Speak("Please give another command, or say End Program.",engine)


	# Turning off stream
	#drone.streamoff()

if __name__ == "__main__":
	main()
