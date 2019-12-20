import time
import sys
from easytello import tello

import time
from threading import Thread

def timer(drone):
	print("---Top of timer method---")
	count = 0
	while count < 31:
		time.sleep(10)
		count += 10
		print("Hi, this program has now been running for " + str(count) + " seconds.")
		drone.cw(90)
	print("---We waited for a total of %s seconds" % str(count))
	sys.exit(0)



def main():
	sys.stdout.write("---Top of the main method in tello.py---\n")
	countdown = time.time()
	print("Countdown initialized time of %s" % str(countdown))
	clockwise = None

	connect_bool = False
	while not connect_bool:
		print("---Top of While---")
		drone = tello.Tello()
		print(drone)
		if drone != None:
			connect_bool = True

	print("Hello! Welcome to the program timer!")
	background_thread = Thread(target=timer, args=(drone,))
	background_thread.start()

	drone.takeoff()
	print("---After takeoff---\n")
	for i in range(50):
		#clockwise = drone.cw(90)
		clockwise = "Null"
		print("Sleeping for %s seconds and clockwise status is %s---" % (str(i), str(clockwise)))
		time.sleep(1)

if __name__ == "__main__":
	main()
