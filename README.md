# tello_speech_recognition

Description:
This project accomplishes the task of connecting human speech to tello drone commands. The user can say a command in normal english and this NLP pipeline will be able to map that speech to the corresponding command.

Project Structure:
Main.py:
	This file starts out the program. It begins by connecting the computer to the tello drone. Then it begins an alternate thread that will call the clockwise command to ensure the tello doesn't enter emergency mode after not receiving a command for 15 seconds. Then the main file will call the Recognize method in Speech_Recognition.py. Once the command has been received and the number associated with the movement command is returned then it sends that information to the Process method in Process_Commands.py. This is done in a while loop to take consecutive speech commands.

Speech_Recognition.py:
	This file will use Google's API to listen to the human voice and translate it to text. Then the methods in this file will find the corresponding commands. It also parses out all numbers in the spoken command. The algorithm allows for some error on the part of the speech recognizer. 

Process_Commands.py:
	This file takes in a command and number and command type. The two command types are MOVEMENT and NON_MOVEMENT commands. NON_MOVEMENT commands do not have a number associated with them. This will simply give the correct command to the tello drone and then print out the response from the drone to the console. 

Commands.py:
	This file contains all the commands associated with the drone along with words that will help identify commands spoken in different ways. It also contains a list of all custom commands that the drone could execute.

Custom_Commands.py:
	This file contains the definitions for the custom command methods. 

Computer_Speech.py:
	This file has the script that allows the computer to take in a string of text and then have the computer say it back to the user.
