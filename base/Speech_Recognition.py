import pyttsx3
import re
import speech_recognition   as sr
import Computer_Speech		as cs
import Commands             as co
from playsound import playsound
from fuzzywuzzy import fuzz
#import pocketsphinx

listen_error = "Sorry, I didn't understand that. Please say the command again."

def Recognize():
    engine = pyttsx3.init()


    speech_command = ""
    listening = True
    while listening:
        speech_command, final_number, type = Listen()
        command_confirmed = cs.Respond(speech_command, engine)
        if command_confirmed:
            listening = False
        #print("\n---------Confirmed Speech_Command: %s---------" % speech_command)
    return speech_command, final_number, type

def Listen():
    #print("\n---In the Listen method of Speech_Recognition.py---")
    r = sr.Recognizer()

    # initialisation for computer's ability to speak
    engine = pyttsx3.init()

    result = ""
    fuzzed_list = []
    final_fuz_list = []

    listening = True
    while listening:
        try:

            audio = micListen(r)
            mic_result = r.recognize_google(audio)
            print("\n---Google Result: %s---" % mic_result)

            #-----------Custom Commands Section---------------
            for cust_commands in co.CUSTOM:
                if cust_commands in mic_result.lower():
                    return cust_commands, None, "NON_MOVEMENT"
            #-------------------------------------------------
            if "take off" in mic_result.lower():
                return "takeoff()", None, "NON_MOVEMENT"

            numbers = [float(s) for s in re.findall(r'-?\d+\.?\d*', mic_result)]
            #print("---Numbers list: %s---" % str(numbers))
            mic_result = mic_result.split(" ")

            # #TODO must do conjuctive or negative command checking

            #--------------------Choose which list to look at-------------------
            iter_list = []
            if len(numbers) > 0:                                                # case where numbers are in the command
                iter_list = co.MOVEMENT
            else:
                iter_list = co.NON_MOVEMENT


            #--------------------Iterate over every word in the list compared to every command-------
            for word in mic_result:
                r_list, c_list = Fuzz_It(word, iter_list)
                fuz_tup = (word, c_list, r_list)
                fuzzed_list.append(fuz_tup)

            #print("---Resulting Fuzzed List: %s---" % str(fuzzed_list))

            #-------------------Iterate over all tuples and throw out low ratio entries--------------
            for tup in fuzzed_list:
                r_avg = (tup[2][0] + tup[2][1] + tup[2][2]) / 3
                if r_avg > 85:
                    raise Exception('The word %s is too similiar to at least three commands' % str(tup[0]))
                elif r_avg < 10:
                    continue
                elif tup[2][0] >= 82:
                    final_fuz_list.append(tup[1][0])
            #print("---Resulting Final Fuzzed List: %s---" % str(final_fuz_list))

            # Account for conjuctive command
            final_command, final_number, type = Map_Commands(final_fuz_list, numbers)
            #print("Final processed command: %s and number: %s" % (final_command, str(final_number)))
            if final_command == "":
                raise Exception('No Valid Command Recognized')
            listening = False
        except Exception as e:
            print(str(e))
            print("---Sorry, I didn't understand that. Please say the command again.---")
            cs.Speak(listen_error, engine)
            continue

    return final_command, final_number, type

def Map_Commands(fuz_list, numbers):
    command_builder = ""
    # ---------------------------NON_MOVEMENT commands
    if len(numbers) == 0:
        #print("---Map_Commands Method NON_MOVEMENT Commands---")
        for commands in fuz_list:
            if commands == co.GET:
                command_builder += "get_"
            elif commands == co.SPEED:
                command_builder += "speed()"
            elif commands == co.BATTERY:
                command_builder += "battery()"
            elif commands == co.TIME:
                command_builder += "time()"
            elif commands == co.HEIGHT:
                command_builder += "height()"
            elif commands == co.TEMP or commands == co.TEMPERATURE:
                command_builder += "temp()"
            elif commands == co.ATTITUDE:
                command_builder += "attitude()"
            elif commands == co.BARO or commands == co.BARROW:
                command_builder += "baro()"
            elif commands == co.ACCELERATION:
                command_builder += "acceleration()"
            elif commands == co.TOF or commands == co.TIME_OF_FLIGHT:
                command_builder += "tof()"
            elif commands == co.WIFI:
                command_builder += "wifi()"
            elif commands == co.TAKEOFF or commands == co.TAKE_OFF:
                command_builder += "takeoff()"
            elif commands == co.LAND:
                command_builder += "land()"
            elif commands == co.EMERGENCY:
                command_builder += "emergency()"
            elif commands == co.SURVEILLANCE_MODE:
                command_builder += co.SURVEILLANCE_MODE
            else:
                return None, None, None
        print("Result of Map_Commands Method: %s" % command_builder)
        if command_builder == "get_":
            command_builder = "Failed"
        return command_builder, None, "NON_MOVEMENT"

    #----------------------------------MOVEMENT Commands
    elif len(numbers) == 1:
        #print("---Map_Commands Method MOVEMENT Commands---")
        for commands in fuz_list:
            if commands == co.UP or commands == co.UPWARD:
                command_builder = "up(" + str(numbers[0]) + ")"
                break
            elif commands == co.DOWN or commands == co.DOWNWARD:
                command_builder = "down(" + str(numbers[0]) + ")"
                break
            elif commands == co.LEFT:
                command_builder = "left(" + str(numbers[0]) + ")"
                break
            elif commands == co.RIGHT or commands == co.WRITE:
                command_builder = "right(" + str(numbers[0]) + ")"
                break
            elif commands == co.FORWARD:
                command_builder = "forward(" + str(numbers[0]) + ")"
                break
            elif commands == co.BACK or commands == co.BACKWARD:
                command_builder = "back(" + str(numbers[0]) + ")"
                break
            elif commands == co.CW or commands == co.CLOCKWISE:
                command_builder = "cw(" + str(numbers[0]) + ")"
                break
            elif commands == co.CCW or commands == co.COUNTER_CLOCKWISE:
                command_builder = "ccw(" + str(numbers[0]) + ")"
                break
            else:
                continue
        #print("Result of Map_Commands Method: %s" % command_builder)
        return command_builder, numbers[0], "MOVEMENT"
    else:
        print("We have a conjuctive movement command or an error")
        return None, None, None

def Fuzz_It(word, iter_list):
    #print("\n---Current Word: %s" % word)

    first_r = 0
    second_r = 0
    third_r = 0
    first_c = "NO COMMAND"
    second_c = "NO COMMAND"
    third_c = "NO COMMAND"
    r_list = []
    c_list = []

    for commands in iter_list:
        #print("---Current Command: %s---" % commands)
        Str1 = commands
        Str2 = word
        Ratio = fuzz.ratio(Str1.lower(),Str2.lower())   # looks for the direct string similarity

        if Ratio > first_r:
            third_r = second_r
            second_r = first_r
            first_r = Ratio
            third_c = second_c
            second_c = first_c
            first_c = commands
        elif Ratio > second_r:
            third_r = second_r
            second_r = Ratio
            third_c = second_c
            second_c = commands
        elif Ratio > third_r:
            third_r = Ratio
            third_c = commands

    r_list.append(first_r)
    r_list.append(second_r)
    r_list.append(third_r)
    c_list.append(first_c)
    c_list.append(second_c)
    c_list.append(third_c)
    return r_list, c_list

def micListen(r):
    mic = sr.Microphone()
    playsound("listen_noise.mov")
    with mic as source:
        print("\n---Listening...\n")
        return r.listen(source)
