import time
import sys


def surveillance_mode(drone):
    print("\n---Top of surveillance_mode method---\n")
    for i in range(2):
        drone.cw(360)
        drone.wait(2)
        drone.up(100)
        drone.wait(2)
        drone.cw(360)
        drone.wait(2)
        drone.down(100)
        drone.wait(2)
    for j in range(2):
        drone.cw(360)
        drone.wait(2)
        drone.left(50)
        drone.wait(2)
        drone.ccw(360)
        drone.wait(2)
        drone.right(100)
        drone.wait(2)
        drone.cw(360)
        drone.wait(2)
    print("\n---Bottom of surveillance_mode method---")
    print("---Ending surveillance mode---\n")
