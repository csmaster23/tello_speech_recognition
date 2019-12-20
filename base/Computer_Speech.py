import time
import Speech_Recognition 	as sr

command_confirmed = "Command confirmed, execution of command begins."
command_denied = "Command not confirmed. Please say a command."

def Respond(response, engine):
    #print("\n---Top of the Respond Method in Computer_Speech.py---")

    #engine.say("This is what I heard you say.")
    #engine.say(response)
    #engine.say("Is that correct?")
    #engine.runAndWait()

    #speech_command = sr.Listen()
    #speech_command.lower()
    speech_command = "yes"
    if speech_command == "yes" or speech_command == "yeah" or speech_command == "okay" or speech_command == "true" or speech_command == "confirmed" or speech_command == "confirm" or speech_command == "affirmative" or speech_command == "fine" or speech_command == "sure" or speech_command == "good" or speech_command == "yep" or speech_command == "indubitably" or speech_command == "positively" or speech_command == "correct":
        #print("---%s---\n" % command_confirmed)
        #engine.say(command_confirmed)
        #engine.runAndWait()
        return True
    else:
        print("---%s---\n" % command_denied)
        engine.say(command_denied)
        engine.runAndWait()
        return False

def Speak(words, engine):
    engine.say(words)
    engine.runAndWait()
