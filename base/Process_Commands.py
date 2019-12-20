import time
import os
import re
import pyttsx3
import Commands as c
import Custom_Commands as CC

from easytello import tello

# Tello uses cm units by default.

def Process(command, drone, type, number):
    print("\n---Top of Process method in Process_Commands.py---")
    result = ""
    if command == None:             # TODO add if drone == None
        result = "Internal error...command not processed."
    elif type == "NON_MOVEMENT":
        result = execute_non_movement(command, drone)
    elif type == "MOVEMENT":
        result = execute_movement(command, drone, number)
    else:
        result = "Command Type not recognized"
    print("---RESULT OF COMMAND: %s---" % result)


def execute_movement(command, drone, number):
    if number == None:
        return "Number was null, error with the number parsing."
    result = None

    if c.UP in command:
        result = drone.up(number)
        print("---drone.up(%s)---" % str(number))

    elif c.DOWN in command:
        result = drone.down(number)
        print("---drone.down(%s)---" % str(number))

    elif c.FORWARD in command:
        result = drone.forward(number)
        print("---drone.forward(%s)---" % str(number))

    elif c.BACK in command:
        result = drone.back(number)
        print("---drone.back(%s)---" % str(number))

    elif c.LEFT in command:
        result = drone.left(number)
        print("---drone.left(%s)---" % str(number))

    elif c.RIGHT in command:
        result = drone.right(number)
        print("---drone.right(%s)---" % str(number))

    elif c.CLOCKWISE in command:
        result = drone.cw(number)
        print("---drone.cw(%s)---" % str(number))

    elif c.COUNTER_CLOCKWISE in command:
        result = drone.ccw(number)
        print("---drone.ccw(%s)---" % str(number))
    else:
        result = "Invalid Movement Command."

    return result

def execute_non_movement(command, drone):
    result = ""
    if "get_" in command:
        result = getCommands(command, drone)
    else:
        if c.TAKEOFF in command:
            result = drone.takeoff()
        elif c.LAND in command:
            result = drone.land()
        elif c.EMERGENCY in command:
            result = drone.emergency()
        # custom commands now
        elif c.SURVEILLANCE_MODE in command:
            engine = pyttsx3.init()
            engine.say("Entering surveillance mode!")
            engine.runAndWait()
            result = CC.surveillance_mode(drone)
        else:
            result = "Command is not recognized."
    return result

def getCommands(command, drone):
    result = None
    if c.SPEED in command:
        result = drone.get_speed()
        print("---drone.get_speed()---")
    elif c.BATTERY in command:
        result = drone.get_battery()
        print("---drone.get_battery()---")
    elif c.HEIGHT in command:
        result = drone.get_height()
        print("---drone.get_height()---")
    elif c.TEMP in command or c.TEMPERATURE in command:
        result = drone.get_temp()
        print("---drone.get_temp()---")
    elif c.ATTITUDE in command:
        result = drone.get_attitude()
        print("---drone.get_attitude()---")
    elif c.BARO in command:
        result = drone.get_baro()
        print("---drone.get_baro()---")
    elif c.ACCELERATION in command:
        result = drone.get_acceleration()
        print("---drone.get_acceleration()---")
    elif c.WIFI in command:
        result = drone.get_wifi()
        print("---drone.get_wifi()---")
    elif c.TOF in command or c.TIME_OF_FLIGHT in command:
        result = drone.get_tof()
        print("---drone.get_tof()---")
    elif c.IME in command:
        result = drone.get_time()
        print("---drone.get_time()---")
    else:
        result = "Not a valid get request."

    return result




# def Process(command, drone):
#     print("\n---Top of Process method in Process_Commands.py---")
#     # # initialisation for computer's ability to speak
#     #engine = pyttsx3.init()
#
#     command = command.lower()
#     result = None
#
#     # check for get commands
#     if c.GET in command:
#         result = getCommands(command, drone)
#
#     # check for easy commands
#     elif c.TAKEOFF in command or c.TAKE in command or c.TAKE_OFF in command:
#         result = drone.takeoff()
#         print("---drone.takeoff()---")
#     elif c.LAND in command:
#         # do more processing for land (could just have the word in it)
#         result = drone.land()
#         print("---drone.land()---")
#     elif c.EMERGENCY in command:
#         result = drone.emergency()
#         print("---drone.emergency()---")
#
#     # now check for less easy commands
#     else:
#         if c.AND in command:
#             commands = command.split(" and ")
#             result = parse(commands[0], drone)
#             result += parse(commands[1], drone)
#         else:
#             result = parse(command, drone)
#
#     print("\n---Result type: %s---" % type(result))
#     print("---Result: %s---\n" % str(result))
#     # engine.say(result)
#     # engine.runAndWait()



# def parse(command, drone):
#     print("\n---Top of parse method in Process_Commands.py---")
#     result = None
#     numbers = [float(s) for s in re.findall(r'-?\d+\.?\d*', command)]
#     print("---The list of numbers regexed from the input command: %s---\n" % str(numbers))
#     if c.MOVE in command or c.FLY in command or c.GO in command or c.PULL in command or c.DIP in command:
#         if c.UP in command or c.UPWARD in command:
#             if len(numbers) == 1:
#                 #result = drone.up(numbers[0])
#                 print("---drone.up(%s)---" % str(numbers[0]))
#             else:
#                 result = "More than one number."
#         elif c.DOWN in command or c.DOWNWARD in command:
#             if len(numbers) == 1:
#                 result = drone.down(numbers[0])
#                 print("---drone.down(%s)---" % str(numbers[0]))
#             else:
#                 result = "More than one number."
#         elif c.FORWARD in command:
#             if len(numbers) == 1:
#                 result = drone.forward(numbers[0])
#                 print("---drone.forward(%s)---" % str(numbers[0]))
#             else:
#                 result = "More than one number."
#         elif c.BACKWARD in command:
#             if len(numbers) == 1:
#                 result = drone.back(numbers[0])
#                 print("---drone.back(%s)---" % str(numbers[0]))
#             else:
#                 result = "More than one number."
#         elif c.LEFT in command:
#             if len(numbers) == 1:
#                 result = drone.left(numbers[0])
#                 print("---drone.left(%s)---" % str(numbers[0]))
#             else:
#                 result = "More than one number."
#         elif c.RIGHT in command:
#             if len(numbers) == 1:
#                 result = drone.right(numbers[0])
#                 print("---drone.right(%s)---" % str(numbers[0]))
#             else:
#                 result = "More than one number."
#         else:
#             result = "Not a valid movement command."
#     elif c.ROTATE in command or c.SPIN in command or c.TURN in command or c.FLIP_AROUND in command:
#         if c.CLOCKWISE in command:
#             if len(numbers) == 1:
#                 #result = drone.cw(numbers[0])
#                 print("---drone.cw(%s)---" % str(numbers[0]))
#             else:
#                 result = "More than one number."
#         elif c.COUNTER_CLOCKWISE in command:
#             if len(numbers) == 1:
#                 result = drone.ccw(numbers[0])
#                 print("---drone.ccw(%s)---" % str(numbers[0]))
#             else:
#                 result = "More than one number."
#         elif c.FLIP_AROUND in command:
#             pass
#         else:
#             result = "Not a valid turning slash rotating command."
#     elif c.FLIP in command:
#         pass
#     elif c.SURVEILLANCE_MODE in command:
#         engine = pyttsx3.init()
#         engine.say("Entering surveillance mode!")
#         engine.runAndWait()
#         result = CC.surveillance_mode(drone)
#     else:
#         result = "Command is not recognized."
#
#     return result
