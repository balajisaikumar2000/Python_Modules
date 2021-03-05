#pyttsx3 is a library
#which is text to speech library
import  pyttsx3
engine =  pyttsx3.init()

"""RATE"""
#rate =  engine.getProperty('rate')
#print(rate)
#engine.setProperty('rate',125)

"""VOICE"""
#voices = engine.getProperty('voices')      #getting details of current voice

#engine.setProperty('voice',voices[1].id)    #changing index, changes voices. 1 for female


engine.say("hey ....balaji")
engine.runAndWait()





